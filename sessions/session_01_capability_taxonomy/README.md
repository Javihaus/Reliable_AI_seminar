# Session 1: Capability Taxonomy

## What LLMs Can and Cannot Reliably Do

**Date:** Tuesday, January 13, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session establishes the foundational framework for classifying LLM capabilities. We distinguish between tasks that current architectures handle reliably versus those that fail predictably, providing decision criteria for deployment assessment.

## Learning Objectives

By the end of this session, you will be able to:
1. Identify the six capability classes for LLM tasks
2. Assess reliability expectations for each class
3. Classify your deployment scenario using the framework
4. Determine when hybrid architectures are necessary

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_01_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### The Six Capability Classes

1. **Pattern Completion** (HIGH reliability)
   - Text completion, summarization, translation
   - What transformers were designed for

2. **Knowledge Retrieval** (MEDIUM reliability)
   - Factual Q&A, concept explanation
   - Depends on training data coverage

3. **Compositional Reasoning** (LOW reliability)
   - Multi-step proofs, novel algorithms
   - LLMs lack systematic generalization

4. **Continuous State Representation** (VERY LOW reliability)
   - Temporal constraints, scheduling
   - Discrete tokens cannot represent continuous state

5. **Constraint Satisfaction** (LOW reliability)
   - Scheduling, compliance verification
   - Approximation rather than guarantee

6. **Interactive Collaboration** (MEDIUM reliability)
   - Real-time interaction
   - Latency-dependent

## Pre-Session Preparation

1. Complete all setup steps in [setup/](../../setup/)
2. Read: Lake & Baroni (2018) - "Generalization without systematicity"
3. Think about your deployment scenario for the practical exercise

## Practical Exercise

During the session, you will:
1. Describe your deployment scenario
2. Classify it using the capability framework
3. Identify the "weakest link" capability
4. Determine testing requirements

## Deliverable

**Due:** Sunday, January 18, 2026

Submit a **Capability Classification Matrix** for your deployment domain including:
- Task description and context
- Required capability classes
- Reliability assessment for each
- Hybrid architecture determination
- Required testing protocols

## Next Session

Session 2: Architectural Prerequisites for Reliable Performance
