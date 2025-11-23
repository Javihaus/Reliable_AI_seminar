# Session 11: Hybrid Architecture Design II

## Integration Patterns

**Date:** Tuesday, February 17, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session covers implementation patterns for integrating LLM and symbolic components. Students build working prototypes demonstrating hybrid approaches.

## Learning Objectives

By the end of this session, you will be able to:
1. Implement LLM + retrieval (RAG) systems
2. Build LLM + constraint propagation hybrids
3. Create LLM + verification modules
4. Test and validate hybrid systems

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_11_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Integration Patterns

#### Pattern 1: RAG (Retrieval-Augmented Generation)
```
Query → Retriever → Context → LLM → Grounded Response
```

#### Pattern 2: LLM + Constraint Solver
```
Input → LLM (extract) → Constraint Solver → Validated Solution
```

#### Pattern 3: LLM + Verification
```
Input → LLM (generate) → Verifier → Accept/Reject/Revise
```

### Testing Hybrid Systems

- Unit test each component separately
- Integration test the full pipeline
- Validate that hybrid addresses the identified limitation
- Measure improvement over LLM-only baseline

### Common Pitfalls

- Over-relying on LLM for tasks it can't do
- Interface mismatch between components
- Missing error handling at boundaries
- Not testing with adversarial inputs

## Pre-Session Preparation

1. Review Session 10 hybrid architecture design
2. Have your architecture specification ready
3. Set up development environment for coding

## Practical Exercise

During the session, you will:
1. Implement a prototype hybrid system
2. Test against your failure mode scenarios
3. Measure improvement over baseline
4. Document integration decisions

## Deliverable

**Due:** Sunday, February 22, 2026

Submit a **Working Prototype** including:
- Source code for hybrid system
- Test results showing improvement
- Integration documentation
- Known limitations and edge cases

## Next Session

Session 12: Risk Documentation and Production Deployment
