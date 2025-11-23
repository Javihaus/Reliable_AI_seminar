# Session 2: Architectural Prerequisites

## Why Next-Token Prediction Fails

**Date:** Thursday, January 15, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session examines why next-token prediction on discrete tokens succeeds for certain tasks but fundamentally fails for others. Understanding architectural prerequisites helps identify when your task requires mechanisms that LLMs lack.

## Learning Objectives

By the end of this session, you will be able to:
1. Distinguish between discrete and continuous representations
2. Identify pattern matching vs computational processes
3. Recognize biological existence proofs for specialized reasoning
4. Apply Lake & Baroni's compositional generalization framework

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_02_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Discrete vs Continuous Representations

| Representation | Works For | Fails For |
|----------------|-----------|-----------|
| Discrete tokens | Text, symbols, categories | Quantities, time, space |
| Continuous values | Magnitudes, durations | Symbolic manipulation |

### Pattern Matching vs Computational Processes

**Pattern Matching (LLM strength):**
- Completing familiar text patterns
- Recalling training data correlations
- Surface-level linguistic transformations

**Computational Processes (LLM weakness):**
- Arithmetic with novel numbers
- Logical inference chains
- Constraint propagation

### Biological Existence Proofs

Nature shows that reliable temporal reasoning requires dedicated mechanisms:
- **Hippocampal time cells:** Fire at specific temporal intervals
- **Cerebellar timing circuits:** Sub-second precision for motor control
- **Interval timing circuits:** Dopaminergic systems for seconds-to-minutes timing

These are computational mechanisms, not pattern matching.

## Pre-Session Preparation

1. Read: Lake & Baroni (2018) - "Generalization without systematicity"
2. Review your capability classification from Session 1
3. Identify tasks in your domain that require continuous representations

## Practical Exercise

During the session, you will:
1. Analyze three deployment scenarios
2. Identify architectural prerequisites for each
3. Determine whether LLMs can provide them
4. Recommend testing protocols or hybrid approaches

## Deliverable

**Due:** Sunday, January 18, 2026

Submit an **Architectural Analysis Document** for your application including:
- Task decomposition into sub-capabilities
- Required representation types (discrete/continuous)
- LLM architectural fit assessment
- Hybrid architecture recommendations

## Next Session

Session 3: Experimental Design I—Constructing Diagnostic Scenarios
