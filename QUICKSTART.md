# EPI Recorder - Quick Start Guide

## ⏱️ The 30-Second Tutorial

### 1. Installation
```powershell
pip install epi-recorder
```

### 2. Record Your First Run
Navigate to your project folder and run your script using `epi record`.
```powershell
# Instead of: python train.py
# Run this:
epi record --out run.epi -- python train.py
```

### 3. See the Result
```powershell
epi view run.epi
```
This opens your browser. You will see:
- A timeline of every step.
- The output logs.
- The files that were created.
- A green "Verified" badge.

---

## 🛠️ Common Commands

| Task | Command |
| :--- | :--- |
| **Record** | `epi record --out <file.epi> -- <command>` |
| **Verify** | `epi verify <file.epi>` |
| **View** | `epi view <file.epi>` |
| **List Keys** | `epi keys list` |
| **Help** | `epi --help` |

## 📦 What gets recorded?
By default, everything you need:
- **API Calls**: OpenAI, Ollama (redacted automatically).
- **Files**: Any file your script writes.
- **Console**: Standard output and error logs.
- **Environment**: Package versions and OS info.
