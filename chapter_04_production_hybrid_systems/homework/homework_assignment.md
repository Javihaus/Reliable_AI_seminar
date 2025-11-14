# Chapter 4 Homework: Design Your Hybrid System

## Overview

Design and implement a hybrid architecture for a production agentic system, incorporating deterministic workflows, LLM reasoning, and EU AI Act compliance.

**Time estimate**: 6-8 hours

---

## Learning Objectives

By completing this homework, you will:

1. Design a hybrid architecture combining deterministic and LLM components
2. Implement confidence-based routing logic
3. Build compliance-ready audit logging
4. Create a production deployment plan
5. Measure and analyze system performance

---

## Assignment

### Part 1: System Design (2 hours)

**Task**: Design a hybrid system for ONE of the following scenarios:

**Option A: Customer Support Triage**
- Classify support tickets into categories
- Route urgent issues to human agents
- Provide automated responses for common issues
- Volume: 1,000 tickets/day

**Option B: Document Classification**
- Classify documents by type and sensitivity
- Extract key metadata
- Flag documents requiring human review
- Volume: 500 documents/day

**Option C: Code Review Assistant**
- Analyze code changes for issues
- Suggest improvements
- Flag security vulnerabilities
- Volume: 200 pull requests/day

**Deliverables**:
1. Architecture diagram showing:
   - Deterministic components
   - LLM components
   - Routing logic
   - Audit logging
2. Written justification (300-500 words) explaining:
   - Why hybrid approach is appropriate
   - Which architectural pattern(s) you chose
   - Expected cost savings vs pure LLM

---

### Part 2: Implementation (3 hours)

**Task**: Implement your hybrid system with the following components:

**Required Components**:

1. **Deterministic Handler**
   - Rule-based logic for routine cases
   - Pattern matching or keyword detection
   - Fast path with <100ms latency

2. **LLM Handler**
   - LLM-based reasoning for complex cases
   - Structured prompts
   - Explanation generation

3. **Router**
   - Confidence-based routing between handlers
   - Configurable threshold
   - Metrics tracking (deterministic vs LLM path usage)

4. **Audit Logger**
   - EU AI Act Article 15 compliant
   - Decision IDs, timestamps, processing paths
   - Privacy-preserving (hash sensitive data)

**Deliverables**:
- Working Python code in Jupyter notebook
- Test on at least 10 sample inputs
- Document code with comments

---

### Part 3: Compliance Implementation (1.5 hours)

**Task**: Ensure your system meets EU AI Act requirements

**Requirements**:

**Article 13 (Transparency)**:
- [ ] User informed when AI is used
- [ ] Explanation provided for each decision
- [ ] Confidence score disclosed

**Article 15 (Logging)**:
- [ ] All decisions logged automatically
- [ ] Unique decision IDs generated
- [ ] Audit trail retrievable by decision ID

**Article 17 (Quality Management)**:
- [ ] Risk event logging capability
- [ ] Performance metrics tracked
- [ ] Validation pass/fail recorded

**Deliverables**:
- Compliance checklist (check all boxes)
- Sample audit log JSON
- Explanation of privacy protections (100-200 words)

---

### Part 4: Production Deployment Plan (1.5 hours)

**Task**: Create a production deployment plan

**Required Sections**:

1. **Phased Rollout**
   - Shadow mode timeline (1-2 weeks)
   - Limited rollout percentage (10% → 50%)
   - Full rollout criteria

2. **Monitoring Dashboard**
   - Key metrics to track
   - Alert conditions and thresholds
   - Visualization requirements

3. **Rollback Plan**
   - Rollback triggers
   - Rollback procedure steps
   - Data migration considerations

4. **Cost Projections**
   - Current baseline cost (pure LLM)
   - Projected hybrid system cost
   - Monthly savings estimate
   - Break-even analysis

**Deliverables**:
- Written deployment plan (750-1000 words)
- Monitoring dashboard mockup or specification

---

## Submission Requirements

**Format**: Single Jupyter notebook + separate deployment plan document

**Files to submit**:
1. `homework_04_[YOUR_NAME].ipynb` - Implementation
2. `deployment_plan_[YOUR_NAME].md` - Deployment plan

**Code requirements**:
- All code must execute without errors
- Include markdown cells explaining each section
- Provide clear setup instructions

**Deadline**: [To be provided by instructor]

**Submission method**: [Email or GitHub PR]

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| System Design | 20 | Clear architecture, sound justification, appropriate pattern selection |
| Implementation | 35 | Working code, all components present, good code quality |
| Compliance | 20 | All requirements met, privacy protections implemented |
| Deployment Plan | 20 | Comprehensive, realistic, includes monitoring and rollback |
| Code Quality | 5 | Clean, documented, follows best practices |
| **Total** | **100** | |

---

## Evaluation Criteria

**Excellent (90-100)**:
- Production-ready implementation
- Comprehensive compliance
- Detailed deployment plan
- Professional code quality

**Good (80-89)**:
- Solid implementation with minor gaps
- Compliance requirements met
- Adequate deployment plan
- Clean code

**Satisfactory (70-79)**:
- Basic implementation working
- Most compliance requirements met
- Deployment plan present
- Functional code

**Needs Improvement (<70)**:
- Incomplete implementation
- Missing compliance elements
- Insufficient planning
- Code quality issues

---

## Tips for Success

1. **Start with simple rules**: Don't over-engineer deterministic logic
2. **Test thoroughly**: Use diverse inputs to stress-test routing
3. **Document everything**: Future you will thank present you
4. **Ask questions**: Use office hours or email instructor
5. **Iterate**: Build incrementally, test often

---

## Resources

- Chapter 4 content.md (theory)
- Example notebooks (reference implementations)
- LangChain documentation
- EU AI Act official text

---

## Common Pitfalls to Avoid

1. ❌ Making routing logic too complex
2. ❌ Forgetting to hash sensitive data in logs
3. ❌ Not testing edge cases
4. ❌ Unrealistic cost projections
5. ❌ Skipping deployment plan details

---

## Bonus Opportunities (+10 points)

- Implement co-evolving validation (from Example 2)
- Add performance benchmarking suite
- Create working monitoring dashboard
- Implement A/B testing framework

---

**Good luck! This homework brings together everything from the entire course.**
