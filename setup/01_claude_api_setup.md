# Claude API Setup Guide

## Getting Your Claude API Key

This guide walks you through obtaining and configuring your Anthropic Claude API key for the course.

---

## Step 1: Create an Anthropic Account

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Click "Sign Up" or "Get Started"
3. Complete the registration process
4. Verify your email address

---

## Step 2: Add Payment Method

1. Navigate to **Settings** > **Billing**
2. Add a credit card or payment method
3. Set a usage limit to control costs (recommended: $50-100 for the course)

### Cost Estimates

| Model | Input | Output | Typical Session |
|-------|-------|--------|-----------------|
| Claude Sonnet 4.5 | $3/M tokens | $15/M tokens | $0.50-2.00 |
| Claude Haiku | $0.25/M tokens | $1.25/M tokens | $0.05-0.20 |

**Course Budget:** Plan for approximately $50-100 total over 6 weeks.

---

## Step 3: Generate API Key

1. Go to **Settings** > **API Keys**
2. Click **Create Key**
3. Give it a descriptive name: `production-llm-course`
4. Copy the key immediately (it won't be shown again)
5. Store securely (see below)

---

## Step 4: Secure Storage

### NEVER DO THIS:
```python
# NEVER hardcode API keys in your code!
api_key = "sk-ant-api03-..."  # DANGEROUS!
```

### Google Colab (Recommended for Course)

Use Colab's Secrets feature:

1. Click the **key icon** in the left sidebar
2. Add a new secret named `ANTHROPIC_API_KEY`
3. Paste your API key as the value
4. Toggle "Notebook access" to ON

```python
# In your notebook:
from google.colab import userdata
import anthropic

client = anthropic.Anthropic(
    api_key=userdata.get('ANTHROPIC_API_KEY')
)
```

### Local Development

Use environment variables:

```bash
# Add to ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# Reload shell
source ~/.bashrc
```

```python
# In your code:
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get('ANTHROPIC_API_KEY')
)
```

### Using .env Files (Alternative)

```bash
# Create .env file (add to .gitignore!)
echo "ANTHROPIC_API_KEY=sk-ant-api03-..." > .env
echo ".env" >> .gitignore
```

```python
# In your code:
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY')
```

---

## Step 5: Test Your Key

Run this test script to verify your setup:

```python
import anthropic

client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY env var

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Say 'API key working!' and nothing else."}
    ]
)

print(message.content[0].text)
# Expected output: API key working!
```

---

## API Key Security Checklist

- [ ] API key stored in environment variable or Colab secrets
- [ ] `.env` file added to `.gitignore`
- [ ] Never committed API key to version control
- [ ] Set spending limit in Anthropic console
- [ ] Using course-specific API key (can revoke after course)

---

## Troubleshooting

### "Invalid API Key" Error

1. Check for extra spaces when copying
2. Verify key starts with `sk-ant-api03-`
3. Ensure payment method is valid
4. Try generating a new key

### "Rate Limit" Error

1. Wait 60 seconds and retry
2. Reduce request frequency
3. Check Anthropic status page

### "Insufficient Credits" Error

1. Add payment method
2. Check billing settings
3. Increase spending limit

---

## Claude Model IDs

For this course, we primarily use:

| Model | Model ID | Use Case |
|-------|----------|----------|
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` | Primary model |
| Claude Haiku | `claude-haiku-3-5-20241022` | Quick tests |
| Claude Opus 4 | `claude-opus-4-20250514` | Complex reasoning |

### Extended Thinking (Optional)

For tasks requiring deep reasoning:

```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[{"role": "user", "content": "Complex reasoning task..."}]
)
```

---

## Next Steps

1. Complete [02_environment_setup.md](02_environment_setup.md)
2. Configure [03_colab_configuration.md](03_colab_configuration.md)
3. Run [04_verify_setup.ipynb](04_verify_setup.ipynb) to confirm everything works

---

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com)
- [Claude Model Overview](https://docs.anthropic.com/en/docs/about-claude/models)
- [API Reference](https://docs.anthropic.com/en/api)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
