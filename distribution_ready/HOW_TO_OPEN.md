# 📖 How to Open This .epi File

## ⚠️ IMPORTANT: Don't Open in Code Editors!

**VS Code, Notepad++, and other code editors will show binary garbage** because .epi files are ZIP archives with a special structure.

---

## ✅ Method 1: Use the EPI Viewer (Recommended)

### If you have EPI installed:

```bash
# Install EPI Recorder first
pip install epi-recorder

# View the file (opens in browser automatically)
epi view sec_compliant_aapl_trade.epi
```

**This is the easiest way!** It automatically opens the interactive viewer in your browser.

---

## ✅ Method 2: Manual Unzip (No Installation Required)

### ⚠️ CRITICAL: Windows doesn't show "Extract All" for .epi files!

**You MUST rename it to .zip first!**

#### **Windows (Correct Steps):**

1. **Rename the file:**
   - Right-click `sec_compliant_aapl_trade.epi`
   - Click "Rename"
   - Change it to `sec_compliant_aapl_trade.zip`
   - Click "Yes" when Windows asks if you're sure

2. **Now extract:**
   - Right-click `sec_compliant_aapl_trade.zip`  
   - Click "Extract All..."
   - Choose a destination folder
   - Click "Extract"

3. **Open the viewer:**
   - Navigate to the extracted folder
   - Open the `viewer` folder
   - **Double-click `index.html`** or `viewer.html`
   - It opens in your default browser (Chrome, Edge, Firefox)

**That's it!** The viewer is a standalone HTML file - no internet connection needed.

#### **macOS:**
macOS automatically recognizes .epi files as ZIP archives:

1. Double-click `sec_compliant_aapl_trade.epi` (auto-extracts)
2. Open the extracted folder
3. Navigate to `viewer/index.html`
4. Double-click to open

#### **Linux:**
```bash
# Unzip the file (Linux knows it's a ZIP)
unzip sec_compliant_aapl_trade.epi -d sec_trade_extracted

# Open viewer in browser
xdg-open sec_trade_extracted/viewer/index.html
```


---

## ✅ Method 3: Inspect the Contents

If you want to **explore the internal structure** (for technical understanding):

1. **Rename** `sec_compliant_aapl_trade.epi` to `sec_compliant_aapl_trade.zip`
2. **Extract** using any ZIP tool
3. You'll see:
   ```
   ├── mimetype              ← File type identifier
   ├── manifest.json         ← Metadata + cryptographic signature
   ├── steps.jsonl           ← Step-by-step execution log
   ├── stdout.log            ← Console output
   ├── environment.json      ← System info
   └── viewer/
       └── index.html        ← Interactive viewer (OPEN THIS!)
   ```
4. **Open** `viewer/index.html` in your browser

---

## 🔍 What You'll See

Once you open the viewer, you'll see:

- **Interactive Timeline**: Every step of the trading decision
- **Cryptographic Signature**: Proof the evidence is tamper-proof
- **Complete Metadata**: When, where, and how it was recorded
- **Execution Details**: Market analysis, risk checks, trade execution

---

## ❓ Verify the Signature

Want to prove it's tamper-proof?

```bash
# Install EPI
pip install epi-recorder

# Verify cryptographic signature
epi verify sec_compliant_aapl_trade.epi

# Expected output:
# ✅ Signature: Valid
# ✅ Integrity: Verified
```

**Try tampering:**
1. Unzip the file
2. Edit `steps.jsonl` (change any value)
3. Re-zip it
4. Run `epi verify` again
5. Watch it fail! ❌ Signature will be invalid

---

## 🚫 Common Mistakes

### ❌ Opening in VS Code
**Problem:** Shows binary data (PK��...)  
**Solution:** Use Method 2 above - unzip and open viewer/index.html

### ❌ Double-clicking the .epi file
**Problem:** Windows doesn't know how to open it  
**Solution:** Right-click → "Extract All" or use `epi view` command

### ❌ Looking for a "readable" file
**Problem:** .epi is a container format (like .docx or .xlsx)  
**Solution:** The viewer IS the readable format - open viewer/index.html

---

## 💡 Think of .epi Like a .docx File

| File Type | What It Really Is | How to Open |
|-----------|-------------------|-------------|
| **.docx** | ZIP with XML files | Microsoft Word |
| **.xlsx** | ZIP with XML files | Excel |
| **.epi** | ZIP with JSON + HTML | **Unzip → Open viewer/index.html** |

You wouldn't open a .docx in Notepad and expect to read it - same with .epi files!

---

## 🎯 Quick Reference Card

```
┌─────────────────────────────────────────────┐
│  HOW TO VIEW .EPI FILES                     │
├─────────────────────────────────────────────┤
│                                             │
│  Option A (with EPI installed):            │
│    epi view filename.epi                    │
│                                             │
│  Option B (no installation):               │
│    1. Unzip the .epi file                   │
│    2. Open viewer/index.html in browser     │
│                                             │
│  ❌ DON'T open in code editors!             │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 🆘 Still Stuck?

- **Discord**: [Join our community](https://discord.gg/epilabs)
- **GitHub Issues**: [Report a problem](https://github.com/mohdibrahimaiml/EPI-V2.0.0/issues)
- **Email**: epitechforworld@outlook.com

---

**Pro Tip:** Bookmark this page! Share it with anyone who asks "How do I open this .epi file?"
