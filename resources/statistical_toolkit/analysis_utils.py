"""
Statistical Analysis Utilities for LLM Risk Characterization

Production LLM Deployment: Risk Characterization Before Failure
"""

import numpy as np
import pandas as pd
from scipy import stats
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class TestResult:
    """Container for a single test result."""
    test_id: str
    expected: str
    actual: str
    correct: bool
    prompt_format: str = "default"
    model: str = "unknown"
    latency_ms: float = 0.0


@dataclass
class StatisticalSummary:
    """Container for statistical analysis results."""
    n: int
    accuracy: float
    ci_lower: float
    ci_upper: float
    false_positive_rate: float
    false_negative_rate: float
    brittleness_score: float
    cohens_d: Optional[float] = None


def calculate_accuracy_with_ci(
    results: List[TestResult],
    confidence: float = 0.95
) -> Tuple[float, float, float]:
    """
    Calculate accuracy with confidence interval using Wilson score interval.

    Args:
        results: List of test results
        confidence: Confidence level (default 0.95)

    Returns:
        Tuple of (accuracy, ci_lower, ci_upper)
    """
    n = len(results)
    if n == 0:
        return 0.0, 0.0, 0.0

    successes = sum(1 for r in results if r.correct)
    p_hat = successes / n

    # Wilson score interval
    z = stats.norm.ppf(1 - (1 - confidence) / 2)
    denominator = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denominator
    margin = z * np.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * n)) / n) / denominator

    ci_lower = max(0, center - margin)
    ci_upper = min(1, center + margin)

    return p_hat, ci_lower, ci_upper


def calculate_false_positive_rate(
    results: List[TestResult],
    negative_label: str = "NO"
) -> float:
    """
    Calculate false positive rate.

    FPR = FP / (FP + TN) = incorrectly positive / actually negative

    Args:
        results: List of test results
        negative_label: Label indicating negative/no-action case

    Returns:
        False positive rate (0-1)
    """
    negatives = [r for r in results if r.expected == negative_label]
    if not negatives:
        return 0.0

    false_positives = sum(1 for r in negatives if not r.correct)
    return false_positives / len(negatives)


def calculate_false_negative_rate(
    results: List[TestResult],
    positive_label: str = "YES"
) -> float:
    """
    Calculate false negative rate.

    FNR = FN / (FN + TP) = incorrectly negative / actually positive

    Args:
        results: List of test results
        positive_label: Label indicating positive/action case

    Returns:
        False negative rate (0-1)
    """
    positives = [r for r in results if r.expected == positive_label]
    if not positives:
        return 0.0

    false_negatives = sum(1 for r in positives if not r.correct)
    return false_negatives / len(positives)


def calculate_brittleness(
    results_by_format: Dict[str, List[TestResult]]
) -> float:
    """
    Calculate brittleness score as max accuracy difference across formats.

    Args:
        results_by_format: Dict mapping format name to results

    Returns:
        Brittleness score (percentage points)
    """
    if len(results_by_format) < 2:
        return 0.0

    accuracies = []
    for format_name, results in results_by_format.items():
        if results:
            acc = sum(1 for r in results if r.correct) / len(results)
            accuracies.append(acc)

    if len(accuracies) < 2:
        return 0.0

    return (max(accuracies) - min(accuracies)) * 100


def calculate_cohens_d(group1: List[float], group2: List[float]) -> float:
    """
    Calculate Cohen's d effect size.

    Args:
        group1: First group of values
        group2: Second group of values

    Returns:
        Cohen's d effect size
    """
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return 0.0

    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

    # Pooled standard deviation
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))

    if pooled_std == 0:
        return 0.0

    return (mean1 - mean2) / pooled_std


def perform_statistical_test(
    group1: List[float],
    group2: List[float],
    test_type: str = "ttest"
) -> Dict:
    """
    Perform statistical significance test.

    Args:
        group1: First group of values
        group2: Second group of values
        test_type: Type of test ("ttest", "mannwhitney", "chi2")

    Returns:
        Dict with test statistic and p-value
    """
    if test_type == "ttest":
        statistic, p_value = stats.ttest_ind(group1, group2)
    elif test_type == "mannwhitney":
        statistic, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')
    else:
        raise ValueError(f"Unknown test type: {test_type}")

    return {
        "test_type": test_type,
        "statistic": statistic,
        "p_value": p_value,
        "significant_05": p_value < 0.05,
        "significant_01": p_value < 0.01,
        "cohens_d": calculate_cohens_d(group1, group2)
    }


def analyze_results(
    results: List[TestResult],
    confidence: float = 0.95
) -> StatisticalSummary:
    """
    Perform comprehensive statistical analysis of test results.

    Args:
        results: List of test results
        confidence: Confidence level for intervals

    Returns:
        StatisticalSummary object
    """
    accuracy, ci_lower, ci_upper = calculate_accuracy_with_ci(results, confidence)
    fpr = calculate_false_positive_rate(results)
    fnr = calculate_false_negative_rate(results)

    # Group by format for brittleness
    by_format = {}
    for r in results:
        if r.prompt_format not in by_format:
            by_format[r.prompt_format] = []
        by_format[r.prompt_format].append(r)

    brittleness = calculate_brittleness(by_format)

    return StatisticalSummary(
        n=len(results),
        accuracy=accuracy,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        false_positive_rate=fpr,
        false_negative_rate=fnr,
        brittleness_score=brittleness
    )


def detect_bimodal_distribution(
    values: List[float],
    threshold: float = 0.3
) -> Dict:
    """
    Detect if distribution is bimodal using Hartigan's dip test approximation.

    Args:
        values: List of numeric values
        threshold: Threshold for bimodality detection

    Returns:
        Dict with bimodality indicators
    """
    if len(values) < 10:
        return {"bimodal": False, "reason": "Insufficient data"}

    values = np.array(values)

    # Simple approach: check for two distinct clusters
    median = np.median(values)
    below = values[values < median]
    above = values[values >= median]

    if len(below) < 3 or len(above) < 3:
        return {"bimodal": False, "reason": "Unbalanced distribution"}

    # Check gap between clusters
    gap = np.min(above) - np.max(below)
    range_val = np.max(values) - np.min(values)

    if range_val == 0:
        return {"bimodal": False, "reason": "No variance"}

    gap_ratio = gap / range_val

    return {
        "bimodal": gap_ratio > threshold,
        "gap_ratio": gap_ratio,
        "threshold": threshold,
        "lower_cluster_mean": np.mean(below),
        "upper_cluster_mean": np.mean(above)
    }


def generate_report(
    results: List[TestResult],
    system_name: str = "LLM System"
) -> str:
    """
    Generate a formatted statistical report.

    Args:
        results: List of test results
        system_name: Name of system being tested

    Returns:
        Formatted report string
    """
    summary = analyze_results(results)

    report = f"""
================================================================================
STATISTICAL ANALYSIS REPORT: {system_name}
================================================================================

SAMPLE SIZE: {summary.n} test cases

ACCURACY METRICS
----------------
Overall Accuracy: {summary.accuracy:.1%}
95% Confidence Interval: [{summary.ci_lower:.1%}, {summary.ci_upper:.1%}]

ERROR RATES
-----------
False Positive Rate: {summary.false_positive_rate:.1%}
False Negative Rate: {summary.false_negative_rate:.1%}

BRITTLENESS
-----------
Brittleness Score: {summary.brittleness_score:.1f} percentage points
(Maximum accuracy difference across prompt formats)

INTERPRETATION
--------------
"""

    # Add interpretation
    if summary.accuracy >= 0.9:
        report += "- Accuracy: HIGH (>90%)\n"
    elif summary.accuracy >= 0.7:
        report += "- Accuracy: MODERATE (70-90%)\n"
    else:
        report += "- Accuracy: LOW (<70%) - DEPLOYMENT RISK\n"

    if summary.false_positive_rate > 0.2:
        report += "- False Positive Rate: HIGH (>20%) - CRITICAL for safety applications\n"

    if summary.brittleness_score > 20:
        report += "- Brittleness: HIGH (>20pp) - Pattern matching, not robust understanding\n"
    elif summary.brittleness_score > 10:
        report += "- Brittleness: MODERATE (10-20pp) - Some format sensitivity\n"
    else:
        report += "- Brittleness: LOW (<10pp) - Relatively robust to format changes\n"

    report += "\n" + "=" * 80 + "\n"

    return report


# Convenience function for quick analysis
def quick_analyze(
    expected: List[str],
    actual: List[str],
    formats: Optional[List[str]] = None
) -> StatisticalSummary:
    """
    Quick analysis from lists of expected and actual values.

    Args:
        expected: List of expected values
        actual: List of actual values
        formats: Optional list of format names

    Returns:
        StatisticalSummary object
    """
    if formats is None:
        formats = ["default"] * len(expected)

    results = [
        TestResult(
            test_id=str(i),
            expected=e,
            actual=a,
            correct=(e == a),
            prompt_format=f
        )
        for i, (e, a, f) in enumerate(zip(expected, actual, formats))
    ]

    return analyze_results(results)


if __name__ == "__main__":
    # Example usage
    example_results = [
        TestResult("1", "YES", "YES", True, "natural"),
        TestResult("2", "NO", "YES", False, "natural"),
        TestResult("3", "YES", "YES", True, "clinical"),
        TestResult("4", "NO", "NO", True, "clinical"),
        TestResult("5", "YES", "NO", False, "json"),
        TestResult("6", "NO", "YES", False, "json"),
    ]

    report = generate_report(example_results, "Example LLM System")
    print(report)
