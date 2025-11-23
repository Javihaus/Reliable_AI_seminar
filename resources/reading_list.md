# Course Reading List

## Production LLM Deployment: Risk Characterization Before Failure

---

## Required Reading

### Foundational Papers

1. **Lake, B. M., & Baroni, M. (2018)**
   "Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks."
   *International Conference on Machine Learning (ICML)*

   **Key Concepts:** Compositional generalization, SCAN benchmark, systematic vs statistical learning

   **Read for Sessions:** 1, 2, 3

2. **Allen, J. F. (1983)**
   "Maintaining knowledge about temporal intervals."
   *Communications of the ACM, 26(11), 832-843*

   **Key Concepts:** Interval algebra, 13 temporal relations, constraint propagation

   **Read for Sessions:** 5, 10

3. **Marín, J. (2025)**
   "Empirical Characterization of Temporal Constraint Processing in LLMs."
   *arXiv preprint*

   **Key Concepts:** Bimodal performance, prompt brittleness, action bias

   **Read for Sessions:** 5, 9

4. **Marín, J. (2025)**
   "The Confidence-Competence Gap in Language Model Scaling."
   *arXiv preprint*

   **Key Concepts:** Scaling pathology, CCG metric, loss-accuracy divergence

   **Read for Sessions:** 6, 9

---

## Recommended Reading

### LLM Capabilities and Limitations

5. **Wei, J., et al. (2022)**
   "Emergent Abilities of Large Language Models."
   *Transactions on Machine Learning Research (TMLR)*

   **Key Concepts:** Emergence, phase transitions, unpredictable capabilities

6. **Schaeffer, R., et al. (2023)**
   "Are Emergent Abilities of Large Language Models a Mirage?"
   *NeurIPS 2023*

   **Key Concepts:** Metric choice, smooth scaling, emergence as artifact

7. **Kaplan, J., et al. (2020)**
   "Scaling Laws for Neural Language Models."
   *arXiv preprint*

   **Key Concepts:** Power laws, compute-optimal training, predictable scaling

8. **Hoffmann, J., et al. (2022)**
   "Training Compute-Optimal Large Language Models."
   *NeurIPS 2022* (Chinchilla paper)

   **Key Concepts:** Data scaling, optimal model size, training efficiency

### Reasoning and Planning

9. **Valmeekam, K., et al. (2023)**
   "On the Planning Abilities of Large Language Models."
   *NeurIPS 2023*

   **Key Concepts:** Planning limitations, blocksworld, task decomposition failures

10. **Dziri, N., et al. (2023)**
    "Faith and Fate: Limits of Transformers on Compositionality."
    *NeurIPS 2023*

    **Key Concepts:** Compositional tasks, multi-step reasoning, error propagation

11. **Shanahan, M. (1997)**
    *Solving the Frame Problem: A Mathematical Investigation of the Common Sense Law of Inertia*
    MIT Press

    **Key Concepts:** Frame problem, temporal reasoning, situation calculus

    **Read:** Chapters 1-3 for Sessions 5, 10

### Reliability and Safety

12. **Ji, Z., et al. (2023)**
    "Survey of Hallucination in Natural Language Generation."
    *ACM Computing Surveys*

    **Key Concepts:** Hallucination taxonomy, detection methods, mitigation

13. **Perez, E., et al. (2022)**
    "Red Teaming Language Models with Language Models."
    *EMNLP 2022*

    **Key Concepts:** Automated red teaming, failure discovery, adversarial testing

14. **Anthropic. (2025)**
    "Claude Sonnet 4.5 Model Card."

    **Key Concepts:** Capabilities, limitations, safety evaluations

### Hybrid Architectures

15. **Lewis, P., et al. (2020)**
    "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."
    *NeurIPS 2020*

    **Key Concepts:** RAG architecture, knowledge grounding, retrieval integration

16. **Yao, S., et al. (2023)**
    "ReAct: Synergizing Reasoning and Acting in Language Models."
    *ICLR 2023*

    **Key Concepts:** Reasoning traces, tool use, interleaved generation

17. **Nakano, R., et al. (2021)**
    "WebGPT: Browser-assisted question-answering with human feedback."
    *arXiv preprint*

    **Key Concepts:** Tool augmentation, verification, human feedback

### Evaluation and Testing

18. **Liang, P., et al. (2022)**
    "Holistic Evaluation of Language Models (HELM)."
    *arXiv preprint*

    **Key Concepts:** Multi-metric evaluation, standardized benchmarks, taxonomy

19. **Ribeiro, M. T., et al. (2020)**
    "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList."
    *ACL 2020*

    **Key Concepts:** Behavioral testing, capability testing, minimum functionality

### Regulatory and Compliance

20. **European Commission. (2024)**
    "Regulation (EU) 2024/1689 - The AI Act."
    *Official Journal of the European Union*

    **Key Concepts:** Risk classification, high-risk requirements, compliance

21. **NIST. (2023)**
    "AI Risk Management Framework (AI RMF 1.0)."

    **Key Concepts:** Risk management, governance, trustworthy AI

---

## Additional Resources

### Technical Documentation

- [Anthropic Claude Documentation](https://docs.anthropic.com)
- [LangChain Documentation](https://python.langchain.com)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

### Online Courses and Tutorials

- [Stanford CS324: Large Language Models](https://stanford-cs324.github.io/winter2022/)
- [DeepLearning.AI: LangChain for LLM Application Development](https://www.deeplearning.ai/)

### Blogs and Updates

- [Anthropic Research Blog](https://www.anthropic.com/research)
- [LangChain Blog](https://blog.langchain.dev/)
- [The Gradient](https://thegradient.pub/)

---

## Reading Schedule

| Week | Required Reading | Recommended |
|------|-----------------|-------------|
| 1 | Lake & Baroni (2018) | Wei et al. (2022), Schaeffer et al. (2023) |
| 2 | — | Ribeiro et al. (2020), Kaplan et al. (2020) |
| 3 | Marín - Temporal (2025), Allen (1983) | Valmeekam et al. (2023) |
| 4 | Marín - CCG (2025) | Ji et al. (2023), Dziri et al. (2023) |
| 5 | Shanahan Ch. 1-3 | Lewis et al. (2020), Yao et al. (2023) |
| 6 | EU AI Act (selected) | NIST AI RMF |

---

*Papers marked as required will be discussed in live sessions. Come prepared with questions and observations.*
