# Upload Instructions

## 1. GitHub Releases

1. Go to: https://github.com/mohdibrahimaiml/EPI-V2.0.0/releases
2. Click "Draft a new release"
3. Tag: `v2.1.1-sample`
4. Title: "Sample EPI File - SEC-Compliant Trading Evidence"
5. Description:
```markdown
## 📦 Download the Sample

**⚠️ IMPORTANT: Don't open in VS Code!** - See HOW_TO_OPEN.md below for viewing instructions.

This is a real, cryptographically signed .epi evidence package.

### How to View:
1. Download `sec_compliant_aapl_trade.epi`
2. Right-click → "Extract All" (or unzip)
3. Open `viewer/index.html` in any browser

**Or use the CLI:** `pip install epi-recorder` then `epi view sec_compliant_aapl_trade.epi`

### What's Inside:
- SEC-compliant trading decision ($89,100 AAPL trade)
- Market analysis, risk assessment, compliance checks
- Cryptographic Ed25519 signature
- Interactive timeline viewer

**Try tampering with it** - edit any file and watch the signature verification fail!
```

6. Upload these files:
   - `sec_compliant_aapl_trade.epi` (the sample file)
   - `HOW_TO_OPEN.md` (viewing instructions)
   - `README.md` (quick overview)
7. Publish!

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
