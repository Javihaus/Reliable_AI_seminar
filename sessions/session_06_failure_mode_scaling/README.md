# Session 6: Failure Mode II—Knowledge Scaling Pathology

## The Confidence-Competence Gap

**Date:** Thursday, January 29, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session examines the confidence-competence gap: why models become more confident in wrong answers as they scale. Understanding when scaling won't help is critical for deployment decisions.

## Learning Objectives

By the end of this session, you will be able to:
1. Identify tasks exhibiting scaling pathology
2. Calculate the confidence-competence gap metric
3. Recognize when larger models won't help
4. Recommend appropriate model sizes by task type

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_06_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### The Scaling Pathology

Counterintuitive finding: On certain tasks, larger models:
- Have lower loss (seem more capable)
- Have worse or flat accuracy (actually fail more confidently)
- Exhibit higher confidence on wrong answers

### Confidence-Competence Gap (CCG)

The CCG quantifies this phenomenon:

$$CCG = \frac{\partial L / \partial N}{\partial A / \partial N}$$

Where L = loss, A = accuracy, N = model size.

- CCG ≈ -48 observed in our experiments
- Negative CCG means: confidence increases while accuracy decreases

### Task Categories

| Task Type | Scaling Behavior | Recommendation |
|-----------|------------------|----------------|
| Pattern completion | Improves with scale | Use larger models |
| Knowledge retrieval | Mixed | Test before scaling |
| Temporal reasoning | Pathological | Don't scale, use hybrid |
| Compositional | Pathological | Don't scale, use hybrid |

## Pre-Session Preparation

1. Review Sessions 4-5 results
2. Read: Kaplan et al. (2020) "Scaling Laws for Neural Language Models"
3. Optional: Schaeffer et al. (2023) "Are Emergent Abilities a Mirage?"

## Practical Exercise

During the session, you will:
1. Test multiple model sizes on your task
2. Plot loss vs accuracy curves
3. Calculate CCG for your domain
4. Determine if scaling helps your task

## Deliverable

**Due:** Sunday, February 8, 2026

Submit a **Scaling Analysis Report** documenting:
- Performance by model size (at least 3 sizes)
- Loss vs accuracy analysis
- CCG calculation with interpretation
- Recommendation: scale or use hybrid?

## Next Session

Session 7: Failure Mode III—Prompt Brittleness and Pattern Matching
