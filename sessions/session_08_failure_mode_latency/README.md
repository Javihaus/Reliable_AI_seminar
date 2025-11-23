# Session 8: Failure Mode IV—Response Latency

## Interaction Constraints and Bandwidth Degradation

**Date:** Thursday, February 5, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session characterizes how response delays create fundamental bandwidth constraints independent of response quality. We examine how latency affects human-AI collaboration and interactive applications.

## Learning Objectives

By the end of this session, you will be able to:
1. Quantify latency impact on interaction bandwidth
2. Measure collaboration efficiency degradation
3. Understand human cognitive timing expectations
4. Design for latency constraints

## Materials

| Resource | Description |
|----------|-------------|
| [recitation.tex](recitation.tex) | LaTeX source for recitation document |
| [recitation.pdf](../../docs/rendered_recitations/session_08_recitation.pdf) | Rendered PDF |
| [notebook.ipynb](notebook.ipynb) | Interactive Colab notebook |

## Key Concepts

### Bandwidth Degradation

Empirical finding: Response latency degrades interaction bandwidth:
- 0s delay: 7.43 turns/minute
- 5s delay: 4.89 turns/minute (34% drop)
- 10s delay: 3.28 turns/minute (56% drop)

### Effect Size

Cohen's d up to 5.973 across cognitive domains—this is a massive, consistent effect.

### Pure Additive Delay

Key finding: Humans don't adapt or compensate. The delay is purely additive—no strategic adjustment occurs.

### Cognitive Expectations

Human interaction timing expectations:
- Conversational turns: 200-500ms gaps
- Collaborative work: 1-3s acceptable
- Beyond 10s: Significant workflow disruption

## Pre-Session Preparation

1. Think about latency in your deployment scenario
2. Measure typical response times for your models
3. Consider your users' interaction patterns

## Practical Exercise

During the session, you will:
1. Measure latency for different prompt complexities
2. Simulate interaction bandwidth at various delays
3. Calculate task completion impact
4. Design latency mitigation strategies

## Deliverable

**Due:** Sunday, February 8, 2026

Submit a **Latency Impact Analysis** including:
- Response time measurements for your application
- Bandwidth degradation estimates
- User experience impact assessment
- Mitigation strategy recommendations

## Next Session

Session 9: Comprehensive Failure Mode Catalog
