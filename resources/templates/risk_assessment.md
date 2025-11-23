# Risk Assessment Template

## Production LLM Deployment Risk Assessment

---

## System Identification

**System Name:** _________________________________

**Version:** _________________________________

**Assessment Date:** _________________________________

**Assessor:** _________________________________

---

## 1. Executive Summary

*Provide a one-page summary of the risk assessment findings.*

### Overall Risk Level: [ ] Low [ ] Medium [ ] High [ ] Critical

### Key Findings:
1. _________________________________
2. _________________________________
3. _________________________________

### Critical Risks Requiring Immediate Attention:
1. _________________________________
2. _________________________________

### Recommended Actions:
1. _________________________________
2. _________________________________
3. _________________________________

---

## 2. System Description

### 2.1 Purpose and Intended Use
_________________________________

### 2.2 Target Users
- Primary users: _________________________________
- Secondary users: _________________________________

### 2.3 Deployment Environment
- [ ] Cloud-hosted
- [ ] On-premise
- [ ] Hybrid
- [ ] Edge deployment

### 2.4 Integration Points
| System | Integration Type | Data Exchanged |
|--------|-----------------|----------------|
| | | |
| | | |

### 2.5 Data Processed
- Input types: _________________________________
- Output types: _________________________________
- Sensitive data categories: [ ] PII [ ] PHI [ ] Financial [ ] Other: _______

---

## 3. Capability Limitations

### 3.1 Tasks System Can Reliably Perform
| Task | Reliability | Evidence |
|------|-------------|----------|
| | High/Medium/Low | |
| | | |

### 3.2 Tasks System Cannot Reliably Perform
| Task | Failure Mode | Consequence |
|------|--------------|-------------|
| | | |
| | | |

### 3.3 Architectural Limitations
| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Temporal reasoning | | |
| Compositional reasoning | | |
| Constraint satisfaction | | |
| Other: | | |

---

## 4. Failure Mode Analysis

### 4.1 Identified Failure Modes

#### Failure Mode 1: _________________________________

| Attribute | Value |
|-----------|-------|
| Description | |
| Trigger conditions | |
| Likelihood | [ ] Rare [ ] Unlikely [ ] Possible [ ] Likely [ ] Almost Certain |
| Impact severity | [ ] Negligible [ ] Minor [ ] Moderate [ ] Major [ ] Catastrophic |
| Detection method | |
| Current controls | |
| Residual risk | |

#### Failure Mode 2: _________________________________

| Attribute | Value |
|-----------|-------|
| Description | |
| Trigger conditions | |
| Likelihood | [ ] Rare [ ] Unlikely [ ] Possible [ ] Likely [ ] Almost Certain |
| Impact severity | [ ] Negligible [ ] Minor [ ] Moderate [ ] Major [ ] Catastrophic |
| Detection method | |
| Current controls | |
| Residual risk | |

#### Failure Mode 3: _________________________________

| Attribute | Value |
|-----------|-------|
| Description | |
| Trigger conditions | |
| Likelihood | [ ] Rare [ ] Unlikely [ ] Possible [ ] Likely [ ] Almost Certain |
| Impact severity | [ ] Negligible [ ] Minor [ ] Moderate [ ] Major [ ] Catastrophic |
| Detection method | |
| Current controls | |
| Residual risk | |

### 4.2 Failure Mode Summary Matrix

| Failure Mode | Likelihood | Severity | Risk Score | Priority |
|--------------|------------|----------|------------|----------|
| | | | | |
| | | | | |
| | | | | |

*Risk Score = Likelihood × Severity (1-25 scale)*

---

## 5. Quantified Risk Metrics

### 5.1 Testing Results Summary

| Metric | Value | Confidence Interval | Acceptable Threshold |
|--------|-------|--------------------|--------------------|
| Overall Accuracy | | | |
| False Positive Rate | | | |
| False Negative Rate | | | |
| Brittleness Score | | | |
| Hallucination Rate | | | |

### 5.2 Comparative Analysis

| Metric | This System | Industry Benchmark | Gap |
|--------|-------------|-------------------|-----|
| | | | |
| | | | |

---

## 6. Mitigation Measures

### 6.1 Technical Mitigations

| Risk | Mitigation | Implementation Status | Owner |
|------|------------|----------------------|-------|
| | | [ ] Planned [ ] In Progress [ ] Complete | |
| | | | |

### 6.2 Operational Mitigations

| Risk | Mitigation | Implementation Status | Owner |
|------|------------|----------------------|-------|
| | | | |
| | | | |

### 6.3 Human Oversight Requirements

| Scenario | Required Oversight | Escalation Path |
|----------|-------------------|-----------------|
| | | |
| | | |

---

## 7. Residual Risk Assessment

### 7.1 Residual Risks After Mitigation

| Risk | Initial Level | After Mitigation | Acceptable? |
|------|---------------|------------------|-------------|
| | | | [ ] Yes [ ] No |
| | | | |

### 7.2 Risk Acceptance

**Residual risks accepted by:** _________________________________

**Date:** _________________________________

**Conditions for acceptance:**
1. _________________________________
2. _________________________________

---

## 8. Monitoring Requirements

### 8.1 Key Risk Indicators

| KRI | Threshold | Monitoring Frequency | Alert Recipient |
|-----|-----------|---------------------|-----------------|
| | | | |
| | | | |

### 8.2 Incident Triggers

| Event | Severity | Required Action |
|-------|----------|-----------------|
| | | |
| | | |

---

## 9. Review Schedule

| Review Type | Frequency | Next Review Date |
|-------------|-----------|------------------|
| Full assessment | Annual | |
| Metric review | Monthly | |
| Incident review | Per incident | |

---

## 10. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Risk Assessor | | | |
| Technical Lead | | | |
| Business Owner | | | |
| Compliance Officer | | | |

---

## Appendices

- [ ] A: Detailed testing results
- [ ] B: Statistical analysis
- [ ] C: Architecture diagrams
- [ ] D: Compliance checklist
- [ ] E: Incident response procedures
