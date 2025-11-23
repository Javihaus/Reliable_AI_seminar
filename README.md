<div align="center">

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/e47ec1fe-be03-498a-ae2c-f8d33cf16cdc" />

# Production LLM Deployment: Risk Characterization Before Failure

### Systematic Methodology for High-Stakes AI Applications

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
![Anthropic Claude](https://img.shields.io/badge/Claude-Sonnet%204.5-191919?style=for-the-badge&logo=anthropic&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-Notebooks-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=for-the-badge)](https://langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agents-FF6B35?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow?style=for-the-badge)](LICENSE)


[![Course Status](https://img.shields.io/badge/Status-Enrolling%20Now-brightgreen?style=for-the-badge)](https://maven.com)
[![Start Date](https://img.shields.io/badge/Starts-January%202026-blue?style=for-the-badge)](#course-schedule)
[![Enroll Now](https://img.shields.io/badge/Enroll%20Now-Limited%20to%2025%20Students-ff6b6b?style=for-the-badge)](#enrollment)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/YOUR_INVITE)

[![Email](https://img.shields.io/badge/Email-javier%40jmarin.info-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:javier@jmarin.info)
___
</div>



<img width="70" height="70" alt="image" src="https://github.com/user-attachments/assets/f7d72454-5fa4-4a14-9201-67a0259b4cbc" />


## Course Overview


Organizations deploy large language models in production assuming benchmarks predict real-world performance. **This assumption causes catastrophic failures.** This course teaches systematic methodology for characterizing architectural limitations before deployment—distinguishing genuine capability from brittle pattern matching, identifying failure modes through rigorous experimentation, and designing hybrid systems when pure LLMs fundamentally cannot work.

> **What This Course Is:** Systematic risk characterization methodology for production LLM deployment in high-stakes applications.
>
> **What This Course Is Not:** Prompt engineering recipes, fine-tuning tutorials, or methods to improve LLM architectures. We document what current approaches cannot reliably do.

### What You Will Learn

**Week 1-2: Foundations & Experimental Design**
- Classify LLM capabilities: what works reliably vs what fails predictably
- Understand architectural prerequisites for different task types
- Design experiments that reveal production failure modes before deployment
- Perform statistical analysis distinguishing genuine capability from spurious patterns

**Week 3-4: Failure Mode Deep Dives**
- Temporal constraint processing failures and bimodal performance distributions
- Knowledge scaling pathology: the confidence-competence gap
- Prompt brittleness as diagnostic for pattern matching
- Response latency and interaction bandwidth constraints

**Week 5-6: Hybrid Architectures & Production Deployment**
- Design LLM + symbolic reasoning hybrid systems
- Implement integration patterns (RAG, constraint propagation, verification modules)
- Document risks for EU AI Act compliance and regulatory review
- Build production monitoring protocols

### Tools & Technologies (2025-2026 Stack)

| Category | Tools |
|----------|-------|
| **LLM APIs** | Claude Sonnet 4.5, Claude Agent SDK, OpenAI GPT-4o |
| **Agentic Frameworks** | LangChain 0.3+, LangGraph, Claude Agent SDK |
| **RL/Alignment** | DPO, GRPO, RLHF evaluation frameworks |
| **Observability** | LangSmith, Weights & Biases, custom telemetry |
| **Compute** | Google Colab Pro, local Python environments |
| **Compliance** | EU AI Act 2026 documentation templates |

___

<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/c14e0783-541c-4f6e-84af-0560876480ee" />

## Prerequisites

### Technical Requirements
- **Production ML experience** (deployed at least one model to production)
- **Python programming** (can read and adapt experimental code)
- **Basic statistics** (hypothesis testing, p-values, confidence intervals)
- **Familiarity with LLM APIs** and prompt engineering

### Required Tools
- Google Colab account (Pro recommended for faster execution)
- **Your own Claude API key** from [Anthropic Console](https://console.anthropic.com)
- GitHub account (to access course materials)
- Python 3.10+ local environment (optional but recommended)

### Expected Time Commitment
- **Live sessions:** 18 hours (12 sessions x 90 minutes)
- **Office hours:** 6 hours (weekly 60-minute sessions)
- **Homework:** 3-4 hours per week
- **Final project:** 8-10 hours

### API Cost Estimate
Students should budget approximately **$50-100** for API usage throughout the course when running experiments with their own API keys.

___

<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/23dc2163-9975-4734-9bad-ec7ca88dd9d4" />

## Course Schedule

**Duration:** 6 weeks | **Format:** Live cohort (max 25 students)

### Week 1: Foundations
| Session | Topic | Date |
|---------|-------|------|
| 1 | Capability Taxonomy—What LLMs Can and Cannot Reliably Do | Tue, Jan 13, 2026 |
| 2 | Architectural Prerequisites for Reliable Performance | Thu, Jan 15, 2026 |

### Week 2: Experimental Design
| Session | Topic | Date |
|---------|-------|------|
| 3 | Experimental Design I—Constructing Diagnostic Scenarios | Tue, Jan 20, 2026 |
| 4 | Experimental Design II—Statistical Analysis and Causal Testing | Thu, Jan 22, 2026 |

### Week 3: Failure Modes I
| Session | Topic | Date |
|---------|-------|------|
| 5 | Failure Mode I—Temporal Constraint Processing | Tue, Jan 27, 2026 |
| 6 | Failure Mode II—Knowledge Scaling Pathology | Thu, Jan 29, 2026 |

### Week 4: Failure Modes II
| Session | Topic | Date |
|---------|-------|------|
| 7 | Failure Mode III—Prompt Brittleness and Pattern Matching | Tue, Feb 3, 2026 |
| 8 | Failure Mode IV—Response Latency and Interaction Constraints | Thu, Feb 5, 2026 |

### Week 5: Hybrid Architectures
| Session | Topic | Date |
|---------|-------|------|
| 9 | Comprehensive Failure Mode Catalog | Tue, Feb 10, 2026 |
| 10 | Hybrid Architecture Design I—LLM + Symbolic Reasoning | Thu, Feb 12, 2026 |

### Week 6: Production & Deployment
| Session | Topic | Date |
|---------|-------|------|
| 11 | Hybrid Architecture Design II—Integration Patterns | Tue, Feb 17, 2026 |
| 12 | Risk Documentation and Production Deployment | Thu, Feb 19, 2026 |

**All sessions:** 10:00 AM - 11:30 AM PST / 6:00 PM - 7:30 PM UTC

See [CALENDAR.md](CALENDAR.md) for complete schedule including office hours.

___

<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/47af1986-5798-48fd-85dc-5c782f83327d" />

## Setup Instructions

Complete all setup steps before the first session:

1. **Read Prerequisites**: [PREREQUISITES.md](PREREQUISITES.md)
2. **Get Claude API Key**: [setup/01_claude_api_setup.md](setup/01_claude_api_setup.md)
3. **Install Dependencies**: [setup/02_environment_setup.md](setup/02_environment_setup.md)
4. **Configure Colab**: [setup/03_colab_configuration.md](setup/03_colab_configuration.md)
5. **Verify Setup**: Run [setup/04_verify_setup.ipynb](setup/04_verify_setup.ipynb)


___

<img width="80" height="80" alt="image" src="https://github.com/user-attachments/assets/16a77bf6-af29-4813-861a-01f63d59d068" />

## Repository Structure
```
├── setup/                              # Pre-course setup guides
│   ├── 01_claude_api_setup.md
│   ├── 02_environment_setup.md
│   ├── 03_colab_configuration.md
│   └── 04_verify_setup.ipynb
│
├── sessions/                           # Course sessions (12 total)
│   ├── session_01_capability_taxonomy/
│   │   ├── recitation.tex              # LaTeX source
│   │   ├── recitation.pdf              # Rendered PDF
│   │   ├── notebook.ipynb              # Colab notebook
│   │   └── exercises/
│   ├── session_02_.../
│   └── ...
│
├── final_project/                      # Final project materials
│   ├── project_brief.md
│   ├── rubric.md
│   ├── templates/
│   └── examples/
│
├── resources/                          # Reference materials
│   ├── templates/                      # Documentation templates
│   ├── statistical_toolkit/            # Analysis scripts
│   └── reading_list.md
│
├── docs/                               # Additional materials
│   └── rendered_recitations/           # All PDFs in one place
│
├── SYLLABUS.md                         # Detailed course syllabus
├── PREREQUISITES.md                    # Prerequisites and preparation
├── CALENDAR.md                         # Complete schedule
└── README.md                           # This file
```

## Using This Repository

### For Live Sessions
During live sessions, the instructor demonstrates examples using their own API key. Students follow along and can run experiments with their own keys.

### For Homework and Practice
Students use their own Claude API key to complete homework assignments and experiments. See [setup/03_colab_configuration.md](setup/03_colab_configuration.md) for instructions on managing API keys securely in Google Colab.

### Google Colab Integration
All notebooks are designed for Google Colab. To open any notebook in Colab:

1. Navigate to the notebook file on GitHub
2. Copy the URL
3. Go to https://colab.research.google.com
4. Select "GitHub" tab and paste the URL

Alternatively, click the "Open in Colab" badge at the top of each notebook.


___

<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/a25a3b33-0677-40ca-b304-d8b829f082d0" />

## Final Project

Students conduct a complete risk characterization for a production LLM deployment (their own system or a provided case study).

### Deliverables
1. **Capability Classification Matrix** for deployment domain
2. **Comprehensive Failure Mode Testing Results** with statistical analysis
3. **Hybrid Architecture Design** (if necessary)
4. **Regulatory Documentation** ready for EU AI Act review
5. **Production Monitoring Plan**

See [final_project/project_brief.md](final_project/project_brief.md) for complete requirements.

### Weekly Deliverables
Students submit 6 major deliverables throughout the course:

| Week | Deliverable |
|------|-------------|
| 1 | Capability classification matrix for deployment domain |
| 2 | Test scenario set with experimental protocol |
| 3 | Experimental results with statistical analysis |
| 4 | Brittleness quantification report |
| 5 | Hybrid architecture specification |
| 6 | Production deployment documentation package |


___

<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/dac697bd-286a-4a0f-88fc-2ca52b454516" />

## About the Instructor

**Javier Marín, PhD** bridges theoretical rigor and production engineering. His research characterizes systematic architectural limitations in LLM deployment through peer-reviewed empirical studies. He has consulted for organizations deploying AI in regulated environments (finance, healthcare), focusing on failure prevention through systematic pre-deployment testing.

**Research Areas:**
- Temporal constraint processing failures (bimodal distributions, prompt brittleness)
- Knowledge scaling pathology (confidence-competence gap quantification)
- Response latency bandwidth constraints (collaboration efficiency degradation)
- EU AI Act compliance for high-risk AI systems

**Publications:**
- "Empirical Characterization of Temporal Constraint Processing in LLMs" (2025)
- "The Confidence-Competence Gap in Language Model Scaling" (2025)
- IEEE DSAA research on Hamiltonian neural networks

**Teaching Philosophy:** Scientific pragmatism without confusing motivational messaging. When current architectures fundamentally cannot solve problems, we acknowledge this clearly and teach systematic approaches to hybrid solutions.

**Contact:** javier@jmarin.info

___

## Enrollment

<div align="center">

### Course Details

| | |
|---|---|
| **Price** | $2,800 |
| **Format** | Live cohort (max 25 students) |
| **Duration** | 6 weeks |
| **Start Date** | January 13, 2026 |
| **Live Sessions** | 12 sessions (90 min each) |
| **Office Hours** | Weekly 60-minute sessions |
| **Community** | Private Slack (lifetime access) |

</div>

### What's Included
- All 12 live session recordings
- 12 detailed recitation documents (LaTeX + PDF)
- Experimental code repositories with replication code
- Statistical analysis toolkit
- EU AI Act documentation templates
- Private Slack workspace with lifetime access
- Monthly alumni meetups

### Target Audience
- ML Engineers deploying LLMs in medical, financial, or emergency response systems
- Technical Leaders making architecture decisions for high-stakes applications
- AI Safety Researchers characterizing failure modes systematically
- Consultants advising organizations on LLM deployment risks

___


<img width="80" height="123" alt="image" src="https://github.com/user-attachments/assets/cc04fe4b-ac6b-4279-aef9-d6355f5d639e" />

## License

This course content is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

## Support

For technical questions during the course:
- Open an issue in this repository
- Email: javier@jmarin.info
- Private Slack workspace
- Live Q&A during scheduled sessions

---

**Note**: This is a rigorous, hands-on course focused on scientific methodology. Come prepared to design experiments, analyze data, and engage with production-scale problems. We prioritize accurate risk characterization over optimistic deployment.
