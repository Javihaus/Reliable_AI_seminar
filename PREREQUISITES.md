# Prerequisites

## Production LLM Deployment: Risk Characterization Before Failure

This document outlines the prerequisites for the course. Please review carefully and complete all setup steps before the first session.

---

## Technical Prerequisites

### Required Experience

#### 1. Production ML Experience
You should have deployed at least one machine learning model to production. This includes:
- Understanding of model serving patterns
- Experience with model monitoring and logging
- Familiarity with production failure modes
- Knowledge of A/B testing or canary deployments

**Self-Assessment:** Can you describe a production ML system you've built or maintained?

#### 2. Python Programming
You should be comfortable with:
- Functions, classes, and object-oriented programming
- Working with dictionaries and JSON data structures
- Using external libraries and packages
- Reading and adapting existing code
- Async/await patterns (helpful but not required)

**Self-Assessment:** Can you read a 200-line Python script and understand its logic?

#### 3. Basic Statistics
You should understand:
- Hypothesis testing (null hypothesis, alternative hypothesis)
- P-values and statistical significance
- Confidence intervals
- Basic probability distributions
- Effect sizes (Cohen's d, etc.)

**Self-Assessment:** Can you interpret a p-value of 0.03 in the context of an experiment?

#### 4. LLM APIs and Prompt Engineering
You should have experience with:
- Making API calls to LLM providers (OpenAI, Anthropic, etc.)
- Writing effective prompts
- Understanding tokens and context windows
- Basic prompt engineering techniques

**Self-Assessment:** Have you built an application that uses LLM APIs?

---

## Required Accounts and API Keys

### 1. Claude API Key (Required)

You need your own Anthropic API key to run experiments during the course.

**Setup Steps:**
1. Go to [Anthropic Console](https://console.anthropic.com)
2. Create an account or sign in
3. Navigate to API Keys
4. Create a new API key
5. Store securely (never commit to version control)

**Budget:** Plan for approximately $50-100 in API usage over 6 weeks.

**Pricing (as of late 2025):**
- Claude Sonnet 4.5: $3/M input tokens, $15/M output tokens
- Claude Haiku: $0.25/M input tokens, $1.25/M output tokens

See [setup/01_claude_api_setup.md](setup/01_claude_api_setup.md) for detailed instructions.

### 2. Google Account (Required)

For Google Colab access:
1. Create a Google account if you don't have one
2. Go to [Google Colab](https://colab.research.google.com)
3. Verify you can create and run notebooks

**Recommended:** Google Colab Pro ($10/month) for faster GPU access and longer runtimes.

### 3. GitHub Account (Required)

For accessing course materials:
1. Create account at [GitHub](https://github.com)
2. Configure SSH keys for repository access
3. Clone this repository to verify access

---

## Software Requirements

### Local Development (Optional but Recommended)

While all exercises can be completed in Google Colab, a local environment is useful for longer experiments.

#### Python 3.10+
```bash
# Check your Python version
python --version  # Should be 3.10 or higher

# Using pyenv (recommended)
pyenv install 3.11.6
pyenv global 3.11.6
```

#### Package Manager
We recommend using `uv` for faster dependency management:
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use pip
pip install --upgrade pip
```

#### Core Packages
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install core dependencies
pip install anthropic langchain langgraph langsmith
pip install numpy pandas scipy matplotlib seaborn
pip install jupyter notebook ipykernel
```

See [setup/02_environment_setup.md](setup/02_environment_setup.md) for complete setup.

---

## Hardware Requirements

### Minimum Requirements
- Modern computer (2020 or newer recommended)
- 8GB RAM minimum
- Stable internet connection for API calls
- Webcam and microphone for live sessions

### Recommended
- 16GB RAM for larger local experiments
- SSD storage
- Dual monitor setup for following along

---

## Pre-Course Preparation

### Week Before Course Start

#### 1. Complete All Setup Steps
- [ ] Claude API key obtained and tested
- [ ] Google Colab account verified
- [ ] GitHub repository cloned
- [ ] Local environment set up (optional)
- [ ] Verification notebook runs successfully

#### 2. Run Verification Notebook
Open and run [setup/04_verify_setup.ipynb](setup/04_verify_setup.ipynb) in Google Colab:
- Verifies API key works
- Tests all required packages
- Confirms environment is ready

#### 3. Complete Pre-Course Reading
Review the following before Session 1:
- This prerequisites document
- [Course Syllabus](SYLLABUS.md)
- Anthropic's [Claude Documentation](https://docs.anthropic.com)

#### 4. Identify Your Deployment Scenario
Think about a production LLM deployment scenario you want to analyze:
- What task is the LLM performing?
- What are the stakes of failure?
- What failure modes concern you?

This will be used throughout the course for practical exercises.

---

## Refresher Resources

If you need to brush up on any prerequisites:

### Python
- [Real Python Tutorials](https://realpython.com)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)

### Statistics
- [StatQuest YouTube Channel](https://www.youtube.com/c/joshstarmer)
- Khan Academy Statistics Course

### LLM Basics
- [Anthropic Claude Documentation](https://docs.anthropic.com)
- [Prompt Engineering Guide](https://www.promptingguide.ai)
- [LangChain Documentation](https://python.langchain.com)

### Machine Learning Production
- [Made With ML - MLOps](https://madewithml.com)
- [Full Stack Deep Learning](https://fullstackdeeplearning.com)

---

## Self-Assessment Checklist

Before enrolling, honestly assess whether you meet these prerequisites:

### Technical Skills
- [ ] I have deployed at least one ML model to production
- [ ] I can write and debug Python code independently
- [ ] I understand p-values, confidence intervals, and hypothesis testing
- [ ] I have used LLM APIs (OpenAI, Anthropic, etc.)
- [ ] I can work with JSON data and REST APIs

### Tools
- [ ] I can use Jupyter notebooks / Google Colab
- [ ] I can use Git for version control
- [ ] I can install Python packages and manage environments

### Mindset
- [ ] I want to understand LLM limitations, not just applications
- [ ] I'm prepared to run experiments and analyze data
- [ ] I can dedicate 8-10 hours per week to the course

---

## Getting Help

### Before the Course
- Email: javier@jmarin.info
- Open an issue in this repository

### During the Course
- Private Slack workspace
- Weekly office hours
- Live session Q&A

---

## FAQ

**Q: I'm a data scientist but haven't deployed models to production. Can I still take the course?**

A: The course focuses on production deployment risks. You'll benefit most if you have production experience, but motivated data scientists who understand ML concepts can succeed with extra effort.

**Q: Do I need to know reinforcement learning?**

A: No. We discuss RLHF and related techniques conceptually, but you don't need to implement them.

**Q: Can I use OpenAI instead of Claude?**

A: The course is designed around Claude APIs and the Claude Agent SDK. Most concepts apply to any LLM, but examples and notebooks use Claude. You're welcome to adapt exercises for other providers.

**Q: How much will API usage cost?**

A: Plan for $50-100 over 6 weeks. Costs depend on how many experiments you run. We provide guidance on efficient API usage.

**Q: Is GPU access required?**

A: No. All exercises run on CPU or use API calls to hosted models. Google Colab free tier is sufficient, though Pro is recommended for faster execution.

---

*Complete the setup steps in [setup/](setup/) before the first session.*
