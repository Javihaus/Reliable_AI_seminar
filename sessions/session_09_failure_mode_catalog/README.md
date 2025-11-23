# Session 9: Comprehensive Failure Mode Catalog

## Complete Taxonomy with Detection Protocols

**Date:** Tuesday, February 10, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session synthesizes all failure modes into a comprehensive catalog with detection protocols. Students build complete testing suites for their deployment scenarios.

## Learning Objectives

By the end of this session, you will be able to:
1. Apply the complete failure mode taxonomy
2. Select appropriate detection protocols for each mode
3. Build comprehensive pre-deployment testing suites
4. Prioritize testing based on application requirements

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_09_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Complete Failure Mode Taxonomy

| Failure Mode | Detection Method | Key Metric |
|--------------|------------------|------------|
| Brittleness | Multi-format testing | Max-min accuracy |
| Action Bias | Balanced test sets | FPR/FNR |
| Scaling Pathology | Multi-model testing | CCG |
| Temporal Failures | Allen algebra tests | Constraint accuracy |
| Latency Issues | Response time measurement | Turns/minute |
| Hallucination | Fact verification | Grounding rate |

### Detection Protocol Selection

Choose protocols based on:
- Application domain (medical, financial, etc.)
- Capability classes required
- Risk tolerance
- Regulatory requirements

### Pre-Deployment Testing Suite

A complete suite includes:
1. Balanced scenario tests (FPR/FNR)
2. Multi-format brittleness tests
3. Scaling analysis (if applicable)
4. Domain-specific failure tests
5. Latency benchmarks

## Pre-Session Preparation

1. Compile all test results from Sessions 3-8
2. List failure modes most relevant to your deployment
3. Prioritize by risk level

## Practical Exercise

During the session, you will:
1. Map your application to the failure mode taxonomy
2. Select detection protocols for each relevant mode
3. Build a prioritized testing checklist
4. Create your comprehensive testing suite

## Deliverable

**Due:** Sunday, February 15, 2026

Submit a **Comprehensive Pre-Deployment Testing Suite** including:
- Failure mode applicability assessment
- Detection protocol specifications
- Test scenario inventory
- Expected vs actual results
- Pass/fail criteria definitions

## Next Session

Session 10: Hybrid Architecture Design I—LLM + Symbolic Reasoning
