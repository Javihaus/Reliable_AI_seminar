# Environment Setup Guide

## Setting Up Your Development Environment

This guide covers setting up a local Python environment for the course. While Google Colab is the primary platform, a local setup enables longer experiments and better debugging.

---

## Quick Start (Google Colab Only)

If you're only using Google Colab, skip to [03_colab_configuration.md](03_colab_configuration.md).

---

## Local Environment Setup

### Step 1: Python Installation

#### Recommended: pyenv (Unix/Mac)

```bash
# Install pyenv
curl https://pyenv.run | bash

# Add to shell configuration (~/.bashrc or ~/.zshrc)
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Reload shell
source ~/.bashrc

# Install Python 3.11
pyenv install 3.11.6
pyenv global 3.11.6

# Verify
python --version  # Python 3.11.6
```

#### Windows

1. Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
2. Run installer with "Add Python to PATH" checked
3. Verify: `python --version`

#### Conda (Alternative)

```bash
# Create environment
conda create -n llm-risk python=3.11
conda activate llm-risk
```

---

### Step 2: Create Virtual Environment

```bash
# Navigate to course directory
cd Production_LLM_Deployment

# Create virtual environment
python -m venv venv

# Activate (Unix/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Verify
which python  # Should show venv path
```

---

### Step 3: Install Dependencies

#### Using pip

```bash
# Upgrade pip
pip install --upgrade pip

# Install core dependencies
pip install -r requirements.txt
```

#### Using uv (Faster Alternative)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv pip install -r requirements.txt
```

---

## Requirements File

Create `requirements.txt` in the project root:

```txt
# Core LLM Libraries
anthropic>=0.40.0
langchain>=0.3.0
langgraph>=0.2.0
langchain-anthropic>=0.3.0
langsmith>=0.1.0

# Data Science
numpy>=1.24.0
pandas>=2.0.0
scipy>=1.10.0
scikit-learn>=1.3.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.15.0

# Statistics
statsmodels>=0.14.0

# Jupyter
jupyter>=1.0.0
notebook>=7.0.0
ipykernel>=6.25.0
ipywidgets>=8.1.0

# Utilities
python-dotenv>=1.0.0
tqdm>=4.65.0
pyyaml>=6.0.0
requests>=2.31.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0

# Type Checking (Optional)
mypy>=1.5.0
```

---

### Step 4: Configure Jupyter Kernel

```bash
# Install kernel for this environment
python -m ipykernel install --user --name=llm-risk --display-name="LLM Risk (Python 3.11)"

# Verify kernel is available
jupyter kernelspec list
```

---

### Step 5: IDE Configuration

#### VS Code (Recommended)

1. Install [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2. Install [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
3. Select interpreter: `Ctrl+Shift+P` > "Python: Select Interpreter" > Choose venv

**Recommended settings** (`.vscode/settings.json`):
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "jupyter.notebookFileRoot": "${workspaceFolder}",
    "editor.formatOnSave": true,
    "python.formatting.provider": "black"
}
```

#### PyCharm

1. Open project
2. Settings > Project > Python Interpreter
3. Add Interpreter > Existing Environment > Select venv

---

## Project Structure

```
Production_LLM_Deployment/
├── venv/                   # Virtual environment (don't commit)
├── .env                    # API keys (don't commit)
├── .gitignore
├── requirements.txt
├── setup/
├── sessions/
│   ├── session_01.../
│   │   ├── notebook.ipynb
│   │   └── exercises/
│   └── ...
└── ...
```

---

## Git Configuration

### .gitignore

Ensure these are in `.gitignore`:

```gitignore
# Virtual environment
venv/
.venv/
env/

# API keys and secrets
.env
.env.local
*.pem
*_key.json

# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
```

---

## Verification

Run this script to verify your setup:

```python
# verify_local_setup.py
import sys
print(f"Python: {sys.version}")

# Check core packages
packages = [
    'anthropic',
    'langchain',
    'langgraph',
    'numpy',
    'pandas',
    'scipy',
    'matplotlib',
    'statsmodels'
]

for pkg in packages:
    try:
        module = __import__(pkg)
        version = getattr(module, '__version__', 'unknown')
        print(f"  {pkg}: {version}")
    except ImportError:
        print(f"  {pkg}: NOT INSTALLED")

# Check API key
import os
api_key = os.environ.get('ANTHROPIC_API_KEY')
if api_key:
    print(f"\nANTHROPIC_API_KEY: Set ({len(api_key)} chars)")
else:
    print("\nANTHROPIC_API_KEY: NOT SET")
```

---

## Troubleshooting

### "Module not found" Errors

1. Verify virtual environment is activated
2. Reinstall package: `pip install --force-reinstall <package>`
3. Check Python path: `which python`

### Jupyter Can't Find Kernel

1. Reinstall ipykernel: `pip install ipykernel`
2. Re-register kernel: `python -m ipykernel install --user --name=llm-risk`
3. Restart Jupyter

### Package Conflicts

```bash
# Create fresh environment
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Next Steps

1. Configure [03_colab_configuration.md](03_colab_configuration.md)
2. Run [04_verify_setup.ipynb](04_verify_setup.ipynb)
3. You're ready for Session 1!
