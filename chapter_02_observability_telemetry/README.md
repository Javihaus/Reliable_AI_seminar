# Chapter 2: Observability & Telemetry

This chapter teaches students how to build monitoring infrastructure for multi-agent AI systems.

## Contents

- **content.md**: Complete theory content (8 sections, ~60 min)
- **examples/**: Live demonstration notebooks
  - `example_01_langchain_callbacks.ipynb`: Building custom callbacks from scratch
  - `example_02_cost_tracking_dashboard.ipynb`: Visualizing cost and performance metrics
  - `example_03_failure_pattern_detection.ipynb`: Automated pattern detection
- **homework/**: Assignment materials
  - `homework_assignment.md`: Instructions and requirements
  - `homework_notebook.ipynb`: Student template
  - `homework_solution.ipynb`: Reference solution

## Learning Objectives

By the end of this chapter, students will be able to:

1. Implement LangChain callbacks to track agent behavior in real-time
2. Build cost tracking dashboards for multi-agent systems
3. Detect failure patterns automatically using telemetry data
4. Design observability infrastructure that scales to production

## Prerequisites

- Complete Chapter 1 and homework
- Understanding of agent failure modes from Chapter 1
- Working Claude API key and LangChain installation
- Basic familiarity with pandas and matplotlib

## Time Allocation

- **Theory**: 35 minutes
- **Live Examples**: 25 minutes
- **Homework**: 3.5-4.5 hours

## Key Concepts

- **Callbacks**: Functions that hook into LLM execution flow
- **Cost Tracking**: Real-time monitoring of token usage and expenses
- **Performance Metrics**: Latency, throughput, success rates
- **Pattern Detection**: Automated identification of failure modes
- **EU AI Act Compliance**: Article 15 logging requirements

## Next Chapter

Chapter 3 uses the telemetry data collected here to crystallize deterministic workflows and achieve 20x cost reductions.
