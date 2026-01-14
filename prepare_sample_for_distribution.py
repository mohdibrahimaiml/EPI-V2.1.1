"""
Quick Distribution Helper for Sample .epi File
This script helps you prepare the sample for distribution
"""

import sys
import io
# Force UTF-8 encoding for Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import shutil
from pathlib import Path
import zipfile

def main():
    print("\n" + "="*70)
    print("  SAMPLE .EPI FILE - DISTRIBUTION HELPER")
    print("="*70 + "\n")
    
    # Paths
    sample_file = Path("epi-recordings/sec_compliant_aapl_trade.epi")
    dist_folder = Path("distribution_ready")
    
    if not sample_file.exists():
        print("[X] Error: Sample file not found!")
        print(f"   Expected: {sample_file.absolute()}")
        return
    
    # Create distribution folder
    dist_folder.mkdir(exist_ok=True)
    
    # 1. Copy the .epi file
    dest_file = dist_folder / "sec_compliant_aapl_trade.epi"
    shutil.copy2(sample_file, dest_file)
    print(f"[OK] Copied .epi file to: {dest_file}")
    
    # 2. Extract viewer for demo
    viewer_folder = dist_folder / "extracted_for_demo"
    viewer_folder.mkdir(exist_ok=True)
    
    with zipfile.ZipFile(sample_file, 'r') as zip_ref:
        zip_ref.extractall(viewer_folder)
    
    print(f"[OK] Extracted contents to: {viewer_folder}")
    print(f"   -> Open this in browser: {viewer_folder / 'viewer' / 'index.html'}")
    
    # 3. Create README for distribution
    readme_content = """# EPI Sample File

## What is this?

This is a **real .epi file** - a cryptographically signed evidence package created by EPI Recorder.

## What's inside?

- **manifest.json**: Metadata and cryptographic signature
- **steps.jsonl**: Step-by-step execution log
- **stdout.log**: Complete console output
- **environment.json**: Python version, OS info, dependencies
- **viewer/index.html**: Interactive timeline viewer

## How to view it?

### Option 1: Just unzip and open

1. Unzip this file (it's a ZIP archive)
2. Open `viewer/index.html` in any web browser
3. Explore the interactive timeline!

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
"""
    
    readme_file = dist_folder / "README.md"
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"[OK] Created README: {readme_file}")
    
    # 4. Create upload instructions
    upload_instructions = dist_folder / "UPLOAD_INSTRUCTIONS.md"
    instructions = """# Upload Instructions

## 1. GitHub Releases

1. Go to: https://github.com/mohdibrahimaiml/EPI-V2.0.0/releases
2. Click "Draft a new release"
3. Tag: `v2.1.1-sample`
4. Title: "Sample EPI File - SEC-Compliant Trading Evidence"
5. Upload: `sec_compliant_aapl_trade.epi`
6. Publish!

## 2. Website (epilabs.org)

Upload to your server and link as:
```
https://epilabs.org/samples/sec_compliant_aapl_trade.epi
```

## 3. Update README.md

Add download link in main repository README.

## 4. Update Colab Notebook

Add download link at the beginning of your Colab demo.

## Direct Download Link (after upload)

```
https://github.com/mohdibrahimaiml/EPI-V2.0.0/releases/download/v2.1.1-sample/sec_compliant_aapl_trade.epi
```
"""
    
    with open(upload_instructions, 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print(f"[OK] Created upload instructions: {upload_instructions}")
    
    # Summary
    print("\n" + "="*70)
    print("  DISTRIBUTION PACKAGE READY!")
    print("="*70)
    print(f"\nFolder: {dist_folder.absolute()}")
    print("\nContents:")
    print("  1. sec_compliant_aapl_trade.epi  <- Upload this")
    print("  2. README.md                      <- Include this")
    print("  3. UPLOAD_INSTRUCTIONS.md         <- Follow these steps")
    print("  4. extracted_for_demo/            <- Preview the viewer")
    print("\nNext: Follow UPLOAD_INSTRUCTIONS.md to publish!")
    print()

if __name__ == "__main__":
    main()
