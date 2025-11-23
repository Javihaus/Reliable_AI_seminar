# Final Project Grading Rubric

## Production LLM Deployment: Risk Characterization Before Failure

---

## Overview

Total Points: 100

| Component | Weight | Points |
|-----------|--------|--------|
| Capability Classification Matrix | 15% | 15 |
| Failure Mode Testing Results | 25% | 25 |
| Hybrid Architecture Design | 20% | 20 |
| Regulatory Documentation | 25% | 25 |
| Production Monitoring Plan | 15% | 15 |

---

## Detailed Rubric

### 1. Capability Classification Matrix (15 points)

#### Task Description & Context (3 points)
| Score | Criteria |
|-------|----------|
| 3 | Clear, complete description of system purpose, users, and deployment context |
| 2 | Good description with minor gaps |
| 1 | Basic description, missing important context |
| 0 | Insufficient or unclear description |

#### Capability Class Analysis (6 points)
| Score | Criteria |
|-------|----------|
| 6 | All 6 classes analyzed with correct reliability assessments and strong justification |
| 5 | All classes analyzed with minor errors or weak justification for 1-2 classes |
| 4 | 5 classes analyzed correctly |
| 3 | 4 classes analyzed correctly |
| 2 | Major errors in assessment or missing 3+ classes |
| 0-1 | Insufficient analysis |

#### Weakest Link & Hybrid Determination (6 points)
| Score | Criteria |
|-------|----------|
| 6 | Correctly identifies weakest link with evidence; hybrid decision well-justified |
| 5 | Correct identification with good justification |
| 4 | Correct identification with basic justification |
| 3 | Minor errors in identification or justification |
| 2 | Significant errors |
| 0-1 | Incorrect or missing |

---

### 2. Failure Mode Testing Results (25 points)

#### Test Design Quality (7 points)
| Score | Criteria |
|-------|----------|
| 7 | 25+ scenarios, perfectly balanced, comprehensive edge cases |
| 6 | 20-24 scenarios, well-balanced, good edge case coverage |
| 5 | 20 scenarios, balanced, some edge cases |
| 4 | 15-19 scenarios, mostly balanced |
| 3 | 10-14 scenarios or unbalanced distribution |
| 2 | <10 scenarios or severely unbalanced |
| 0-1 | Insufficient testing |

#### Brittleness Testing (6 points)
| Score | Criteria |
|-------|----------|
| 6 | 5+ formats tested, comprehensive analysis, clear brittleness quantification |
| 5 | 4 formats tested, good analysis |
| 4 | 4 formats tested, basic analysis |
| 3 | 3 formats tested |
| 2 | 2 formats tested |
| 0-1 | 1 or no format variation testing |

#### Statistical Analysis (6 points)
| Score | Criteria |
|-------|----------|
| 6 | Complete metrics (accuracy, FPR, FNR, CI, effect sizes), correct interpretation |
| 5 | Most metrics calculated correctly |
| 4 | Basic metrics with confidence intervals |
| 3 | Basic metrics without confidence intervals |
| 2 | Incomplete metrics |
| 0-1 | Missing or incorrect statistical analysis |

#### Documentation & Reproducibility (6 points)
| Score | Criteria |
|-------|----------|
| 6 | Fully reproducible notebook, clear documentation, raw data included |
| 5 | Reproducible with minor gaps in documentation |
| 4 | Mostly reproducible, adequate documentation |
| 3 | Some reproducibility issues |
| 2 | Significant reproducibility issues |
| 0-1 | Not reproducible |

---

### 3. Hybrid Architecture Design (20 points)

*If no hybrid needed, grade the justification document instead*

#### Architecture Design (8 points)
| Score | Criteria |
|-------|----------|
| 8 | Clear diagram, well-reasoned component selection, elegant design |
| 7 | Good diagram and design with minor issues |
| 6 | Adequate diagram, reasonable design |
| 5 | Basic design with some unclear elements |
| 4 | Design present but significant issues |
| 2-3 | Major design problems |
| 0-1 | Missing or unworkable design |

#### Component Specification (6 points)
| Score | Criteria |
|-------|----------|
| 6 | Clear responsibilities for each component, no ambiguity |
| 5 | Mostly clear with minor ambiguity |
| 4 | Adequate specification |
| 3 | Some unclear responsibilities |
| 2 | Significant ambiguity |
| 0-1 | Unclear or missing |

#### Interface & Data Flow (6 points)
| Score | Criteria |
|-------|----------|
| 6 | Complete interface specs, clear data flow, error handling defined |
| 5 | Good specs with minor gaps |
| 4 | Adequate specs |
| 3 | Basic specs with gaps |
| 2 | Incomplete specs |
| 0-1 | Missing or unclear |

#### Alternative: No-Hybrid Justification (20 points total)
| Score | Criteria |
|-------|----------|
| 20 | Strong evidence from testing, comprehensive risk mitigation, clear monitoring |
| 15-19 | Good justification with minor gaps |
| 10-14 | Adequate justification |
| 5-9 | Weak justification |
| 0-4 | Insufficient justification |

---

### 4. Regulatory Documentation (25 points)

#### Executive Summary (4 points)
| Score | Criteria |
|-------|----------|
| 4 | Clear, concise, covers all key points in 1 page |
| 3 | Good summary with minor issues |
| 2 | Basic summary |
| 1 | Incomplete or unclear |
| 0 | Missing |

#### System Description (4 points)
| Score | Criteria |
|-------|----------|
| 4 | Complete description of system, intended use, and limitations |
| 3 | Good description with minor gaps |
| 2 | Basic description |
| 1 | Incomplete |
| 0 | Missing |

#### Risk Assessment (8 points)
| Score | Criteria |
|-------|----------|
| 8 | Comprehensive risk matrix, quantified where possible, well-prioritized |
| 7 | Good risk assessment with minor gaps |
| 6 | Adequate assessment |
| 5 | Basic assessment |
| 3-4 | Incomplete assessment |
| 0-2 | Missing or severely incomplete |

#### Mitigation & Oversight (5 points)
| Score | Criteria |
|-------|----------|
| 5 | Clear mitigation for each risk, appropriate human oversight |
| 4 | Good mitigations with minor gaps |
| 3 | Adequate mitigations |
| 2 | Basic or incomplete |
| 0-1 | Missing |

#### EU AI Act Compliance (4 points)
| Score | Criteria |
|-------|----------|
| 4 | Complete checklist, clear compliance status, action items for gaps |
| 3 | Good coverage with minor gaps |
| 2 | Basic coverage |
| 1 | Incomplete |
| 0 | Missing |

---

### 5. Production Monitoring Plan (15 points)

#### KPI Definition (5 points)
| Score | Criteria |
|-------|----------|
| 5 | Comprehensive KPIs covering accuracy, drift, latency, user satisfaction |
| 4 | Good KPI set with minor gaps |
| 3 | Adequate KPIs |
| 2 | Basic or incomplete KPIs |
| 0-1 | Missing or inappropriate KPIs |

#### Alert Thresholds (4 points)
| Score | Criteria |
|-------|----------|
| 4 | Well-justified thresholds for all KPIs with rationale |
| 3 | Good thresholds with minor gaps in justification |
| 2 | Basic thresholds |
| 1 | Incomplete |
| 0 | Missing |

#### Incident Response (4 points)
| Score | Criteria |
|-------|----------|
| 4 | Clear procedures, escalation paths, rollback plans |
| 3 | Good procedures with minor gaps |
| 2 | Basic procedures |
| 1 | Incomplete |
| 0 | Missing |

#### Evaluation Schedule (2 points)
| Score | Criteria |
|-------|----------|
| 2 | Clear schedule for regular evaluation and testing |
| 1 | Basic schedule |
| 0 | Missing |

---

## Grade Conversion

| Points | Grade |
|--------|-------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| <70 | Incomplete (must resubmit) |

---

## Common Deductions

- **Late submission:** -10% per day (max 3 days)
- **Missing README:** -5 points
- **Wrong file format:** -5 points
- **Unrunnable notebook:** -10 points
- **Missing raw data:** -5 points
- **Plagiarism:** Automatic failure

---

## Appeals

Grade appeals must be submitted within 7 days of grade release with specific criteria-based justification. Contact javier@jmarin.info.
