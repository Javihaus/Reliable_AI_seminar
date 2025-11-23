# Session 7: Failure Mode III—Prompt Brittleness

## When Robust Understanding Fails

**Date:** Tuesday, February 3, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session provides systematic characterization of brittleness as a diagnostic for pattern matching vs robust understanding. We learn to design multi-format tests that reveal brittleness and interpret the results.

## Learning Objectives

By the end of this session, you will be able to:
1. Use brittleness as an architectural diagnostic
2. Design semantically equivalent prompt variations
3. Quantify brittleness with statistical rigor
4. Interpret brittleness across domains

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_07_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Brittleness as Diagnostic

Brittleness reveals whether a model truly understands or is pattern matching:
- **Robust understanding:** Same answer regardless of surface form
- **Pattern matching:** Answer changes with irrelevant format changes

### Designing Semantic Equivalents

Good brittleness tests keep meaning constant while varying:
- Vocabulary (formal vs casual)
- Structure (prose vs bullet points vs JSON)
- Length (verbose vs concise)
- Style (clinical vs conversational)

### Quantifying Brittleness

**Brittleness Score = Max Accuracy - Min Accuracy (across formats)**

| Score | Interpretation |
|-------|----------------|
| 0-10 pp | Robust understanding |
| 10-30 pp | Moderate sensitivity |
| 30-50 pp | High brittleness |
| 50+ pp | Extreme - pure pattern matching |

## Pre-Session Preparation

1. Review Session 4 brittleness analysis
2. Bring 3-5 scenarios from your domain with ground truth
3. Draft 3+ format variations for each scenario

## Practical Exercise

During the session, you will:
1. Create 3-5 prompt variations per scenario
2. Test against Claude Sonnet 4.5
3. Calculate brittleness scores
4. Identify which formats fail

## Deliverable

**Due:** Sunday, February 8, 2026

Submit a **Brittleness Quantification Report** including:
- 5+ test scenarios with 3+ formats each
- Per-scenario and aggregate brittleness scores
- Format-specific accuracy analysis
- Pattern matching evidence assessment

## Next Session

Session 8: Failure Mode IV—Response Latency and Interaction Constraints
