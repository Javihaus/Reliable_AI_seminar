# Final Project: Production Risk Characterization

## Production LLM Deployment: Risk Characterization Before Failure

---

## Overview

The final project requires you to conduct a complete risk characterization for a production LLM deployment. You may analyze your own production system or use one of the provided case studies.

**Objective:** Demonstrate mastery of systematic risk characterization methodology by producing deployment-ready documentation suitable for regulatory review.

---

## Project Options

### Option A: Your Own System
Analyze an LLM system you are building or deploying at your organization. This option provides the most practical value.

**Requirements:**
- Must be a real system (not hypothetical)
- Must have production deployment plans
- Can be in development or already deployed

### Option B: Provided Case Studies

Choose one of the following case studies:

1. **Medical Symptom Triage Chatbot**
   - Recommends emergency vs routine care
   - Handles medication timing questions
   - Must comply with healthcare regulations

2. **Financial Document Analyzer**
   - Extracts metrics from earnings reports
   - Validates compliance with reporting standards
   - Supports investment decisions

3. **Customer Support Agent**
   - Handles product inquiries and complaints
   - Processes refund requests
   - Escalates complex issues to humans

4. **Legal Contract Reviewer**
   - Identifies key terms and obligations
   - Flags potential risks
   - Summarizes contract provisions

---

## Deliverables

### 1. Capability Classification Matrix (15%)

Complete capability analysis including:

- [ ] Task description and deployment context
- [ ] Required capability classes with justification
- [ ] Reliability assessment for each class
- [ ] Identification of "weakest link" capability
- [ ] Hybrid architecture necessity determination

**Format:** Structured document or spreadsheet

### 2. Comprehensive Failure Mode Testing Results (25%)

Design and execute testing protocols:

- [ ] Test scenario design (minimum 20 scenarios)
- [ ] Multi-format brittleness testing (4+ formats)
- [ ] Bias testing (false positive/negative rates)
- [ ] Statistical analysis with confidence intervals
- [ ] Scaling analysis (if applicable)

**Required Metrics:**
- Overall accuracy
- Accuracy by capability class
- Brittleness score (percentage point variation)
- False positive rate
- False negative rate
- Cohen's d effect sizes (where applicable)

**Format:** Jupyter notebook with results + summary report

### 3. Hybrid Architecture Design (20%)

If testing reveals limitations requiring hybrid approach:

- [ ] Architecture diagram
- [ ] Component responsibilities (LLM vs symbolic)
- [ ] Interface specifications
- [ ] Data flow documentation
- [ ] Fallback and error handling

**Format:** Technical specification document

If hybrid architecture is NOT needed, provide:
- [ ] Justification based on testing results
- [ ] Risk mitigation strategies for pure LLM deployment
- [ ] Monitoring requirements

### 4. Regulatory Documentation (25%)

Production-ready documentation for stakeholder and regulatory review:

- [ ] Executive summary (1 page)
- [ ] System description and intended use
- [ ] Capability limitations and failure modes
- [ ] Risk assessment matrix
- [ ] Mitigation measures
- [ ] Human oversight requirements
- [ ] EU AI Act compliance checklist (if high-risk)

**Format:** PDF document following provided template

### 5. Production Monitoring Plan (15%)

Ongoing monitoring strategy:

- [ ] Key performance indicators (KPIs)
- [ ] Alert thresholds
- [ ] Drift detection approach
- [ ] Incident response procedures
- [ ] Regular evaluation schedule

**Format:** Operational runbook

---

## Grading Rubric

### Capability Classification (15 points)
| Criteria | Excellent (15-13) | Good (12-10) | Adequate (9-7) | Needs Work (<7) |
|----------|------------------|--------------|----------------|-----------------|
| Completeness | All classes analyzed | Most classes | Some missing | Major gaps |
| Accuracy | Correct assessments | Minor errors | Some errors | Significant errors |
| Justification | Strong evidence | Good reasoning | Basic reasoning | Weak/missing |

### Testing Results (25 points)
| Criteria | Excellent (25-22) | Good (21-17) | Adequate (16-12) | Needs Work (<12) |
|----------|------------------|--------------|----------------|-----------------|
| Test design | Comprehensive, balanced | Good coverage | Basic coverage | Insufficient |
| Statistical rigor | Full analysis | Most metrics | Basic metrics | Missing analysis |
| Brittleness testing | 4+ formats tested | 3 formats | 2 formats | 1 format only |
| Documentation | Clear, reproducible | Mostly clear | Some gaps | Hard to follow |

### Hybrid Architecture (20 points)
| Criteria | Excellent (20-17) | Good (16-13) | Adequate (12-9) | Needs Work (<9) |
|----------|------------------|--------------|----------------|-----------------|
| Design quality | Well-reasoned | Good design | Basic design | Unclear |
| Component clarity | Clear responsibilities | Mostly clear | Some ambiguity | Confused |
| Feasibility | Implementable | Mostly feasible | Questions remain | Not feasible |

### Regulatory Documentation (25 points)
| Criteria | Excellent (25-22) | Good (21-17) | Adequate (16-12) | Needs Work (<12) |
|----------|------------------|--------------|----------------|-----------------|
| Completeness | All sections | Most sections | Some missing | Major gaps |
| Clarity | Publication-ready | Minor edits needed | Needs revision | Unclear |
| Risk assessment | Comprehensive | Good coverage | Basic | Incomplete |
| Compliance | Full checklist | Most items | Some items | Missing |

### Monitoring Plan (15 points)
| Criteria | Excellent (15-13) | Good (12-10) | Adequate (9-7) | Needs Work (<7) |
|----------|------------------|--------------|----------------|-----------------|
| KPIs | Comprehensive | Good set | Basic | Insufficient |
| Thresholds | Well-justified | Reasonable | Basic | Missing |
| Procedures | Clear, actionable | Mostly clear | Some gaps | Unclear |

---

## Submission Requirements

### Format
- Single ZIP file containing all deliverables
- PDF for documents, .ipynb for notebooks
- README.md listing all files

### Naming Convention
```
final_project_[lastname]_[firstname].zip
├── README.md
├── 01_capability_classification.pdf
├── 02_testing_results.ipynb
├── 02_testing_summary.pdf
├── 03_hybrid_architecture.pdf (or 03_no_hybrid_justification.pdf)
├── 04_regulatory_documentation.pdf
├── 05_monitoring_plan.pdf
└── appendices/
    ├── raw_data.csv
    └── additional_analysis.ipynb
```

### Deadline
**Friday, February 28, 2026 at 11:59 PM PST**

Late submissions: 10% penalty per day, maximum 3 days late.

---

## Resources

### Templates
- [Capability Classification Template](../resources/templates/capability_matrix.md)
- [Risk Assessment Template](../resources/templates/risk_assessment.md)
- [EU AI Act Checklist](../resources/templates/eu_ai_act_checklist.md)
- [Monitoring Plan Template](../resources/templates/monitoring_plan.md)

### Code
- [Statistical Analysis Toolkit](../resources/statistical_toolkit/)
- [Testing Framework](../resources/templates/testing_framework.py)

### Reference
- Course recitation documents
- Required readings
- EU AI Act official documentation

---

## FAQ

**Q: Can I work with a partner?**
A: No, the final project is individual work. You may discuss concepts but must produce your own analysis and documentation.

**Q: What if my system doesn't need a hybrid architecture?**
A: Provide a justification document explaining why pure LLM deployment is appropriate based on your testing results.

**Q: How detailed should the testing be?**
A: Minimum 20 test scenarios, 4 prompt formats for brittleness testing. More is better for high-stakes applications.

**Q: What if I can't share proprietary information?**
A: You may anonymize company names, specific data, and sensitive details while preserving the technical analysis.

**Q: Will there be feedback before the deadline?**
A: Submit a draft during Week 5 office hours for preliminary feedback. Final feedback provided after grading.

---

## Contact

Questions about the final project:
- Office Hours: Fridays, 10:00 AM PST
- Email: javier@jmarin.info
- Slack: #final-project channel

---

*Good luck! This project demonstrates the methodology you'll use throughout your career when deploying LLMs in high-stakes applications.*
