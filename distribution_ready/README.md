# EPI Sample File

> **⚠️ DON'T OPEN IN VS CODE OR TEXT EDITORS!**  
> This is a ZIP archive. You'll see binary garbage in code editors.  
> **→ See "How to View" below for the correct way!**

## What is this?

This is a **real .epi file** - a cryptographically signed evidence package created by EPI Recorder.

## What's inside?

- **manifest.json**: Metadata and cryptographic signature
- **steps.jsonl**: Step-by-step execution log
- **stdout.log**: Complete console output
- **environment.json**: Python version, OS info, dependencies
- **viewer/index.html**: Interactive timeline viewer

## How to view it?

### ✅ Option 1: Just Unzip and Open (No Installation!)

**⚠️ Windows Issue: You won't see "Extract All" because Windows doesn't recognize .epi files!**

**CORRECT Steps:**

1. **First, rename** `sec_compliant_aapl_trade.epi` to `sec_compliant_aapl_trade.zip`
   - Right-click → Rename
   - Change extension from `.epi` to `.zip`
   
2. **Now extract:**
   - Right-click the `.zip` file
   - Click "Extract All..."
   - Extract to a folder

3. **Open the viewer:**
   - Go to the extracted folder
   - Open `viewer` folder  
   - **Double-click `index.html`** (opens in your browser)

**That's it!** No installation, no internet required. The viewer is just an HTML file.

### Option 2: Use EPI CLI

```bash
# Install EPI Recorder
pip install epi-recorder

# View the file
epi view sec_compliant_aapl_trade.epi

# Verify the signature
epi verify sec_compliant_aapl_trade.epi
```

## What does this demonstrate?

This sample shows a **SEC-compliant algorithmic trading decision** with:

- Market analysis for AAPL stock
- Risk assessment calculations
- Trade execution details
- MiFID II & Dodd-Frank compliance checks
- Cryptographic Ed25519 signature

## Try tampering with it!

1. Unzip the file
2. Edit any file inside (e.g., `steps.jsonl`)
3. Re-zip it
4. Run `epi verify` on it
5. Watch it fail! The signature will be invalid

**This proves the evidence is tamper-proof.**

## Learn more

- **Website**: https://epilabs.org
- **GitHub**: https://github.com/mohdibrahimaiml/EPI-V2.0.0
- **Docs**: https://epilabs.org/docs
- **PyPI**: https://pypi.org/project/epi-recorder/

---

**Made with love by EPI Labs**
