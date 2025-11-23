# Google Colab Configuration Guide

## Setting Up Google Colab for the Course

Google Colab is the primary platform for course notebooks. This guide covers optimal configuration for running LLM experiments.

---

## Step 1: Access Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Sign in with your Google account
3. Verify you can create a new notebook

---

## Step 2: Configure API Key Storage

### Using Colab Secrets (Recommended)

Colab Secrets provide secure API key storage that persists across sessions.

1. Open any notebook
2. Click the **key icon** (🔑) in the left sidebar
3. Click **"Add new secret"**
4. Configure:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** Your API key (paste from Anthropic Console)
5. Toggle **"Notebook access"** to ON

### Accessing in Code

```python
from google.colab import userdata

# Get API key from secrets
api_key = userdata.get('ANTHROPIC_API_KEY')

# Initialize client
import anthropic
client = anthropic.Anthropic(api_key=api_key)
```

### Alternative: Runtime Input (Less Convenient)

```python
from getpass import getpass
api_key = getpass("Enter your Anthropic API key: ")
```

---

## Step 3: Standard Notebook Header

Use this setup cell at the beginning of every course notebook:

```python
# ============================================
# Production LLM Deployment - Course Setup
# ============================================

# Install required packages (run once per session)
!pip install -q anthropic langchain langgraph langchain-anthropic
!pip install -q numpy pandas scipy matplotlib seaborn statsmodels

# Import core libraries
import anthropic
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import userdata

# Configure plotting
plt.style.use('seaborn-v0_8-whitegrid')
%matplotlib inline

# Initialize Anthropic client
client = anthropic.Anthropic(api_key=userdata.get('ANTHROPIC_API_KEY'))

# Verify connection
try:
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=50,
        messages=[{"role": "user", "content": "Say 'Connected!' only."}]
    )
    print(f"✓ Anthropic API: {response.content[0].text}")
except Exception as e:
    print(f"✗ API Error: {e}")

print("✓ Setup complete!")
```

---

## Step 4: Colab Pro Recommendation

### Free Tier Limitations
- GPU: Limited availability
- RAM: 12.7 GB
- Disk: 78 GB
- Session: Disconnects after ~90 min idle, max 12 hours

### Colab Pro Benefits ($10/month)
- **Priority GPU access** (T4, V100)
- **More RAM:** Up to 32 GB
- **Longer runtimes:** 24+ hours
- **Background execution**

### Colab Pro+ Benefits ($50/month)
- **Premium GPUs:** A100
- **52 GB RAM**
- **Even longer runtimes**

**Recommendation:** Colab Pro is sufficient for this course.

---

## Step 5: Runtime Configuration

### Selecting Runtime Type

1. Go to **Runtime** > **Change runtime type**
2. For most course work: **CPU** is sufficient
3. For scaling experiments: Select **T4 GPU**
4. **High-RAM** toggle: Enable for large datasets

### Managing Sessions

```python
# Check current resources
!cat /proc/meminfo | grep MemTotal
!nvidia-smi  # If GPU enabled

# Mount Google Drive (for saving work)
from google.colab import drive
drive.mount('/content/drive')
```

---

## Step 6: Saving Your Work

### Option 1: Google Drive

```python
# Mount Drive
from google.colab import drive
drive.mount('/content/drive')

# Save notebook outputs
import shutil
shutil.copy('results.csv', '/content/drive/MyDrive/LLM_Course/results.csv')
```

### Option 2: GitHub

1. **File** > **Save a copy in GitHub**
2. Select repository and branch
3. Add commit message

### Option 3: Download Locally

1. **File** > **Download** > **Download .ipynb**

---

## Step 7: Opening Course Notebooks

### From GitHub

1. Go to notebook file in this repository
2. Copy the raw URL
3. In Colab: **File** > **Open notebook** > **GitHub** tab
4. Paste repository URL or search

### Direct Link Pattern

```
https://colab.research.google.com/github/[owner]/Production_LLM_Deployment/blob/main/sessions/session_01/notebook.ipynb
```

---

## Best Practices

### 1. Run Setup Cell First
Always run the setup cell before anything else.

### 2. Save Frequently
Colab can disconnect unexpectedly. Save results to Drive.

### 3. Monitor API Costs
```python
# Track token usage
def log_usage(response):
    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens
    cost = (input_tokens * 3 + output_tokens * 15) / 1_000_000
    print(f"Tokens: {input_tokens} in, {output_tokens} out | Est. cost: ${cost:.4f}")
```

### 4. Use Caching
```python
import pickle
import os

CACHE_FILE = '/content/drive/MyDrive/LLM_Course/cache.pkl'

def cached_call(prompt, cache_key):
    # Load cache
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)

    # Check cache
    if cache_key in cache:
        print("Using cached result")
        return cache[cache_key]

    # Make API call
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.content[0].text

    # Save to cache
    cache[cache_key] = result
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)

    return result
```

### 5. Handle Disconnections
```python
# Wrap long operations
from tqdm import tqdm
import time

results = []
for i, item in enumerate(tqdm(items)):
    try:
        result = process_item(item)
        results.append(result)

        # Save checkpoint every 10 items
        if i % 10 == 0:
            pd.DataFrame(results).to_csv('/content/drive/MyDrive/checkpoint.csv')

    except Exception as e:
        print(f"Error at {i}: {e}")
        time.sleep(5)  # Wait and retry
```

---

## Troubleshooting

### "Secret not found" Error
1. Verify secret name matches exactly (case-sensitive)
2. Ensure "Notebook access" is toggled ON
3. Try restarting the runtime

### Session Disconnected
1. Reconnect via popup
2. Re-run setup cell
3. Load data from Drive checkpoint

### Out of Memory
1. Restart runtime
2. Enable High-RAM
3. Reduce batch sizes
4. Clear unused variables: `del large_variable`

### Slow Package Installation
```python
# Use quiet mode
!pip install -q package_name

# Or install from requirements
!pip install -q -r requirements.txt
```

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Run cell | `Ctrl+Enter` |
| Run cell, move to next | `Shift+Enter` |
| Insert cell above | `Ctrl+M A` |
| Insert cell below | `Ctrl+M B` |
| Delete cell | `Ctrl+M D` |
| Undo | `Ctrl+Z` |
| Find/Replace | `Ctrl+H` |
| Command palette | `Ctrl+Shift+P` |

---

## Next Steps

1. Run [04_verify_setup.ipynb](04_verify_setup.ipynb) to confirm everything works
2. You're ready for Session 1!
