# Session 3: Experimental Design I

## Constructing Diagnostic Scenarios

**Date:** Tuesday, January 20, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session teaches how to design test scenarios that reveal production failure modes before deployment. Well-designed experiments distinguish genuine capability from brittle pattern matching.

## Learning Objectives

By the end of this session, you will be able to:
1. Design balanced test distributions (prevent response bias)
2. Control semantic content while varying format (brittleness tests)
3. Establish deterministic ground truth for evaluation
4. Create scenario sets for your deployment domain

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_03_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Balanced Test Distributions

Unbalanced test sets lead to misleading accuracy:
- If 90% of test cases are positive, a model that always says "YES" gets 90% accuracy
- Always use 50/50 positive/negative splits for binary decisions
- For multi-class, balance across all categories

### Controlling for Confounds

Good experimental design isolates variables:
- **Semantic content:** What the scenario means
- **Surface format:** How it's expressed
- **Complexity:** Number of entities/constraints

### Multi-Format Testing

Test the same scenario in multiple formats:
1. Natural language
2. Clinical/formal style
3. JSON/structured format
4. Conversational style
5. Technical specification

Accuracy variation across formats reveals brittleness.

## Pre-Session Preparation

1. Review Sessions 1-2 materials
2. Identify 3-5 core scenarios from your deployment domain
3. Think about ground truth: How will you know if the answer is correct?

## Practical Exercise

During the session, you will:
1. Design 8-12 test scenarios for your domain
2. Create balanced positive/negative distributions
3. Write each scenario in 3+ formats
4. Establish ground truth labels

## Deliverable

**Due:** Sunday, January 25, 2026

Submit a **Test Scenario Set with Protocol** including:
- 8+ test scenarios with ground truth
- Balanced distribution documentation
- Multi-format variations (3+ formats per scenario)
- Evaluation protocol specification

## Next Session

Session 4: Experimental Design II—Statistical Analysis and Causal Testing
