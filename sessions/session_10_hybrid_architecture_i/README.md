# Session 10: Hybrid Architecture Design I

## LLM + Symbolic Reasoning

**Date:** Thursday, February 12, 2026 | 10:00 AM - 11:30 AM PST

---

## Overview

This session teaches how to design hybrid systems that combine LLMs with explicit symbolic reasoning modules. When pure LLMs fundamentally cannot work, we need different architectures.

## Learning Objectives

By the end of this session, you will be able to:
1. Decide when hybrid architectures are necessary
2. Design LLM + symbolic reasoning systems
3. Implement temporal constraint checkers
4. Specify component responsibilities clearly

## Materials

| Resource | Description |
|----------|-------------|
| recitation.tex | LaTeX source for recitation document |
| notebook.ipynb | Interactive Colab notebook |
| examples/ | Reference implementations |

## Key Concepts

### When Hybrid Architectures Are Necessary

Hybrid is needed when your application requires:
- **Deterministic outputs** for safety-critical decisions
- **Temporal reasoning** (medication timing, scheduling)
- **Constraint satisfaction** (compliance, resource allocation)
- **Verifiable reasoning** (audit requirements)

### Architecture Patterns

#### Pattern 1: LLM + Temporal Constraint Checker
```
User Input → LLM (extract entities) → Symbolic Checker → Validated Output
```

#### Pattern 2: LLM + Verification Module
```
User Input → LLM (generate response) → Verifier → Approved/Rejected
```

#### Pattern 3: LLM + Retrieval (RAG)
```
User Input → Retriever → LLM (with context) → Grounded Response
```

### Component Responsibilities

| Component | Handles | Does NOT Handle |
|-----------|---------|-----------------|
| LLM | Natural language understanding | Temporal math |
| LLM | Entity extraction | Constraint propagation |
| LLM | Human-readable explanations | Verification |
| Symbolic | Temporal constraint checking | NLU |
| Symbolic | Deterministic validation | Ambiguity resolution |
| Symbolic | Audit logging | Natural language generation |

## Pre-Session Preparation

1. Review Session 5 (Temporal Constraint Processing)
2. Read: Shanahan (1997) Chapters 1-3
3. Bring your failure mode test results from Session 9

## Practical Exercise

Design a hybrid architecture for your application:
1. Define component responsibilities
2. Specify interfaces between components
3. Design data flow
4. Plan error handling and fallbacks

## Deliverable

**Due:** Sunday, February 15, 2026

Submit a **Hybrid Architecture Specification** including:
- Architecture diagram
- Component specifications
- Interface definitions
- Data flow documentation
- Error handling plan

## Code Example

```python
class HybridTemporalReasoner:
    def __init__(self, llm_client, symbolic_checker):
        self.llm = llm_client
        self.checker = symbolic_checker

    def reason(self, natural_language_input: str) -> Dict:
        # Step 1: LLM extracts structured information
        extracted = self.llm.extract_temporal_info(natural_language_input)

        # Step 2: Symbolic checker validates constraints
        validation = self.checker.validate(extracted)

        # Step 3: Return deterministic result
        return {
            "input": natural_language_input,
            "extracted": extracted,
            "is_valid": validation.is_valid,
            "explanation": validation.explanation
        }
```

## Next Session

Session 11: Hybrid Architecture Design II - Integration Patterns
