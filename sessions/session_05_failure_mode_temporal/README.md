# Session 5: Failure Mode I—Temporal Constraint Processing

## Why Discrete Tokens Fail for Continuous State

**Date:** Tuesday, January 27, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session provides a deep dive into continuous state representation failures. We examine why discrete tokens cannot reliably handle temporal reasoning, present empirical evidence of systematic failures, and introduce Allen's interval algebra as the foundation for hybrid temporal reasoning systems.

## Learning Objectives

By the end of this session, you will be able to:
1. Understand why LLMs fail on temporal constraint tasks
2. Measure bimodal performance and prompt brittleness
3. Detect systematic action bias in model responses
4. Implement Allen's interval algebra for hybrid architectures

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_05_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Bimodal Performance Distribution

Our experiments reveal that model performance on temporal tasks is bimodal, not continuous:
- Model size does not predict performance
- Phi-3 (3.8B) matches Mistral (7B) at 62.5%
- Llama-2 (7B) fails at 37.5% (below random chance)
- Models either "get it" or they don't

### Extreme Prompt Brittleness

Same semantic content with different formats yields dramatic accuracy changes:
- Natural language: 62.5%
- Clinical note style: 25.0% (-37.5 pp)
- JSON structure: 0.0% (-62.5 pp)

This brittleness proves pattern matching, not reasoning.

### Systematic Action Bias

Models exhibit 100% false positive rates for action recommendations on balanced test sets. When the correct answer is "do not take action," models still recommend action.

### Allen's Interval Algebra

13 basic relations between temporal intervals:
- Before, After
- Meets, Met-by
- Overlaps, Overlapped-by
- During, Contains
- Starts, Started-by
- Finishes, Finished-by
- Equals

## Pre-Session Preparation

1. Review Session 4 (Statistical Analysis)
2. Read: Allen, J. F. (1983). "Maintaining knowledge about temporal intervals."
3. Identify 3 temporal constraints in your deployment scenario

## Practical Exercise

During the session, you will:
1. Test your model on temporal scenarios
2. Measure brittleness across prompt formats
3. Detect action bias
4. Implement a basic hybrid temporal reasoner

## Deliverable

**Due:** Sunday, February 1, 2026

Submit **Temporal Constraint Test Results** including:
- Test scenario set (8+ scenarios, balanced positive/negative)
- Multi-format brittleness measurements
- False positive/negative rates
- Hybrid architecture recommendation

## Next Session

Session 6: Failure Mode II—Knowledge Scaling Pathology
