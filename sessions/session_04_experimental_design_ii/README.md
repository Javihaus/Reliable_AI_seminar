# Session 4: Experimental Design II

## Statistical Analysis and Causal Testing

**Date:** Thursday, January 22, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session teaches rigorous statistical analysis to distinguish genuine capability from spurious patterns. We cover detecting bimodal distributions, quantifying brittleness, measuring bias rates, and conducting causal interventions.

## Learning Objectives

By the end of this session, you will be able to:
1. Detect bimodal distributions (capability vs failure clustering)
2. Quantify prompt brittleness with statistical significance
3. Measure false positive/negative bias rates
4. Design and interpret causal interventions

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_04_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Bimodal Distribution Detection

LLM performance on specific tasks often shows bimodal distributions:
- Models either "get it" (high accuracy) or "don't get it" (low accuracy)
- No continuous improvement with scale
- Use histogram analysis and bimodality tests

### Brittleness Quantification

Brittleness = maximum accuracy - minimum accuracy across formats

| Brittleness | Interpretation |
|-------------|----------------|
| 0-10 pp | Low - robust understanding |
| 10-30 pp | Medium - some format sensitivity |
| 30-50 pp | High - significant pattern matching |
| 50+ pp | Extreme - pure pattern matching |

### Bias Rate Measurement

- **False Positive Rate (FPR):** P(predict positive | actually negative)
- **False Negative Rate (FNR):** P(predict negative | actually positive)
- Critical for high-stakes applications where one type of error is worse

### Causal Interventions

Beyond correlation: manipulate model internals to establish causation:
- Attention manipulation
- Ablation studies
- Activation patching

## Pre-Session Preparation

1. Complete your test scenario set from Session 3
2. Review basic statistics (mean, std, t-test, chi-square)
3. Have your test data ready for analysis

## Practical Exercise

During the session, you will:
1. Run your test suite on 2-3 models
2. Analyze results for bimodality
3. Calculate brittleness metrics
4. Compute FPR and FNR
5. Document failure patterns

## Deliverable

**Due:** Sunday, February 1, 2026

Submit **Experimental Results with Statistical Analysis** including:
- Raw results from multi-model testing
- Bimodality analysis with visualizations
- Brittleness quantification with confidence intervals
- False positive/negative rate calculations
- Failure pattern characterization

## Next Session

Session 5: Failure Mode I—Temporal Constraint Processing
