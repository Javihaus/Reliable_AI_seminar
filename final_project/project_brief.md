# Final Project: Agentic System Audit and Redesign

## Overview

The final project requires you to conduct a complete audit of an existing agentic AI system and propose a production-ready hybrid architecture. This project synthesizes everything learned across all four chapters.

## Objectives

1. Demonstrate systematic diagnosis of agent failures
2. Show observability infrastructure implementation
3. Identify workflow crystallization opportunities
4. Design production-ready hybrid architecture with compliance

## Project Options

### Option A: Your Own System (Recommended)

Audit and redesign an agentic system you have built or are building:
- Real production system (best)
- Internal tool or prototype
- Side project or proof-of-concept

**Benefit**: Directly applicable to your work

### Option B: Provided Case Study

Audit one of the following provided case studies:
- Customer support automation
- Research paper analysis system
- Code review assistant

Case study details: [TO BE PROVIDED IN CLASS]

### Option C: Hypothetical System Design

Design a new system from scratch and analyze it:
- Define use case and requirements
- Design initial architecture
- Audit the design for potential issues

**Requirement**: Must be realistic and detailed

## Deliverables

Submit a single Jupyter notebook containing all sections below.

---

### Section 1: System Description (10 points)

**Content**:
- System purpose and use case
- Current architecture diagram
- Agent roles and responsibilities
- Volume (requests per day)
- Current costs (if known)

**Length**: 300-500 words + diagram

---

### Section 2: Failure Mode Analysis (20 points)

Apply Chapter 1 diagnosis framework:

**Required**:
- Identify at least 3 failure modes from:
  - Temporal coordination failures
  - Cost explosion patterns
  - Prompt brittleness
  - Multi-agent coordination issues

**For each failure mode**:
- Concrete example demonstrating failure
- Root cause analysis
- Impact assessment (cost, reliability, compliance)

**Evidence**: Logs, telemetry, or reproduction steps

---

### Section 3: Observability Implementation (15 points)

Apply Chapter 2 monitoring:

**Required**:
- Implement custom callbacks for monitoring
- Collect telemetry data (minimum 50 requests)
- Generate cost breakdown by agent
- Create 2 visualizations:
  - Cost over time or per-agent breakdown
  - Latency distribution or success rate

**Deliverable**: Working code + visualizations

---

### Section 4: Workflow Crystallization (20 points)

Apply Chapter 3 optimization:

**Required**:
- Identify top 3 crystallization opportunities
- Select one pattern to implement
- Extract decision logic (keywords, rules, or ML)
- Implement deterministic version
- Validate: measure agreement rate with LLM
- Calculate cost savings and ROI

**Acceptance criteria**: ≥90% agreement, measurable cost reduction

---

### Section 5: Hybrid Architecture Design (25 points)

Apply Chapter 4 production patterns:

**Required**:
- Design hybrid architecture (deterministic + LLM)
- Select appropriate architectural pattern:
  - Sequential validation
  - Confidence-based routing
  - Hierarchical decomposition
  - Validation with feedback
- Implement prototype with:
  - Both deterministic and LLM paths
  - Routing logic
  - Audit logging (EU AI Act compliance)
- Test on sample data

**Deliverable**: Working implementation + architecture diagram

---

### Section 6: Production Readiness Assessment (10 points)

**Required**:
- Phased rollout plan (shadow → limited → full)
- Monitoring dashboard requirements
- Alert conditions and thresholds
- Compliance checklist (EU AI Act Articles 13, 15, 17)
- Risk mitigation strategies

**Format**: Structured document, 500-750 words

---

## Evaluation Criteria

Total: 100 points

| Component | Points | Criteria |
|-----------|--------|----------|
| System description | 10 | Clear, detailed, realistic |
| Failure analysis | 20 | Systematic, evidence-based, actionable |
| Observability | 15 | Working code, quality data, clear visualizations |
| Crystallization | 20 | Valid extraction, ≥90% agreement, measurable savings |
| Hybrid architecture | 25 | Sound design, working prototype, compliance-ready |
| Production readiness | 10 | Comprehensive plan, realistic timeline |

**Bonus points** (up to +10):
- Exceptional visualizations or analysis
- Novel insights or techniques
- Implementation beyond requirements
- Production deployment evidence

---

## Submission Requirements

**Format**: Single Jupyter notebook (`final_project_[YOUR_NAME].ipynb`)

**Size limit**: 10MB (excluding large datasets)

**Required sections**: All 6 sections above, in order

**Code requirements**:
- All code must execute without errors
- Include markdown explanations
- Provide clear instructions for running

**Deadline**: [TO BE FILLED]

**Submission method**: [Email to javier@jmarin.info or GitHub PR]

---

## Time Estimate

- System description: 2 hours
- Failure analysis: 3 hours
- Observability: 3 hours
- Crystallization: 4 hours
- Hybrid architecture: 5 hours
- Production readiness: 2 hours
- **Total**: 19-22 hours

**Recommendation**: Start immediately after Day 2. Don't wait until the deadline.

---

## Presentation (30 minutes)

During Day 3 final session, you will present:

**Time**: 5-7 minutes per student

**Content**:
1. System overview (1 min)
2. Key failure mode identified (1 min)
3. Crystallization results (2 min)
4. Hybrid architecture design (2 min)
5. Q&A (1 min)

**Format**: Screen share your notebook + discussion

---

## Grading Rubric

See [evaluation_rubric.md](evaluation_rubric.md) for detailed scoring criteria.

**Grade boundaries**:
- 90-100: Excellent - Production-ready design with clear evidence
- 80-89: Good - Solid work with minor gaps
- 70-79: Satisfactory - Meets requirements but lacks depth
- 60-69: Needs improvement - Missing key components
- <60: Incomplete - Major gaps or non-functional

---

## Resources

**From course**:
- All chapter content and examples
- Homework solutions
- Example notebooks

**External**:
- Your telemetry data from Chapter 2
- LangChain documentation
- EU AI Act official text

**Getting help**:
- Office hours: [TO BE SCHEDULED]
- Email instructor: javier@jmarin.info
- GitHub discussions: [Repository link]

---

## FAQ

**Q: Can I work in a team?**
A: No, this is an individual project. However, you can discuss ideas with classmates.

**Q: Can I use a system I didn't build?**
A: Yes, if you have sufficient access to audit and redesign it.

**Q: What if my system has no failures?**
A: All systems have optimization opportunities. Focus on cost reduction or compliance.

**Q: Can I use a different LLM?**
A: Yes, but explain why and adjust cost calculations accordingly.

**Q: How much code is expected?**
A: Quality over quantity. 200-500 lines of well-documented code is typical.

---

**This is your opportunity to demonstrate mastery of production agentic AI systems. Good luck!**
