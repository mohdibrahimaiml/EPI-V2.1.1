# ✅ Pre-Investor Demo Testing Checklist

**File**: `EPI_DEMO_demo_FIXED.ipynb`  
**Date Fixed**: 2025-12-22  
**Next Investor Meeting**: _____________

---

## 🔍 Critical Tests (DO BEFORE INVESTOR MEETING!)

### Test 1: Fresh Colab Execution
- [ ] Upload `EPI_DEMO_demo_FIXED.ipynb` to Google Colab
- [ ] Click: **Runtime → Restart and run all**
- [ ] Wait for all cells to complete
- [ ] Verify NO red error messages appear

**Expected time**: ~60 seconds

---

### Test 2: Installation Success
- [ ] First cell shows: "✅ EPI Installed from PyPI"
- [ ] NO error message about installation failure
- [ ] Check that it says `epi-recorder` NOT `pandas`

**Critical**: If installation fails, investors can't run the demo!

---

### Test 3: File Download
- [ ] A file named `trade_evidence.epi` downloads to your computer
- [ ] File size is ~14-15 KB
- [ ] Check your Downloads folder to confirm

**Critical**: If no download, the core value prop fails!

---

### Test 4: Signature Verification ⚡ MOST IMPORTANT
- [ ] Demo cell output shows: "✓ FILE IS SIGNED: ..."
- [ ] NO red error message about unsigned file
- [ ] Verify cell output shows Ed25519 signature hash

**Critical**: This is the entire point of the demo. If it says "UNSIGNED", DO NOT show to investors!

---

### Test 5: Viewer Display
- [ ] Viewer loads inside the notebook (interactive HTML)
- [ ] Top banner shows: "🛡️ AUTHENTIC EPI VIEWER"
- [ ] Top banner shows signature hash (ends with "...")
- [ ] Upper right corner badge says: **"Signed"** (green)

**Critical**: If badge says "Unsigned" (yellow), STOP. Fix before showing investors.

---

### Test 6: Viewer Content
- [ ] Left sidebar shows:
  - Workflow ID
  - Created timestamp
  - Files: 2 captured
  - Spec Version: 1.0-keystone
- [ ] Right side shows Timeline with 10 steps
- [ ] Steps include: MARKET_DATA, TECHNICAL, RISK_VAR, COMPLIANCE_SEC, etc.
- [ ] Click on any step - it should expand/show details

---

### Test 7: Tamper Test (Security Demo)
- [ ] Tamper test cell creates `FRAUDULENT_EVIDENCE.epi`
- [ ] Output shows: `epi verify` command running
- [ ] **Verification should FAIL** (returncode != 0 or error message)
- [ ] Final message: "✅ FORGERY DETECTED!"
- [ ] Message says: "Cryptographic verification FAILED as expected"

**Critical**: If it says "Trust Level: HIGH" or "Signature Valid" for the tampered file, that's a BUG. Do NOT show to investors.

---

### Test 8: All Outputs Are Empty
- [ ] In Colab, click: **Edit → Clear all outputs**
- [ ] Scroll through entire notebook
- [ ] Verify NO cell has any output text/graphics
- [ ] All output areas should be blank

**Critical**: Investors MUST see live execution, not pre-recorded results!

---

### Test 9: Visual Quality Check
- [ ] All emojis render correctly (🚀, 💰, ✅, etc.)
- [ ] Tables are properly formatted
- [ ] Colors look professional (no garish bright colors)
- [ ] No weird line breaks or formatting glitches
- [ ] Footer shows: "EPI v2.1.1" (not v2.1.0)

---

### Test 10: Links Work
- [ ] Click: epilabs.org link in footer
- [ ] Click: GitHub link in footer
- [ ] Click: PyPI link in footer
- [ ] Verify all links open correctly

---

## 🚨 Red Flags (STOP if you see these!)

### ❌ Show Stoppers:
1. **"UNSIGNED"** anywhere in viewer or demo output
2. Tamper test shows "Signature Valid" for fraudulent file
3. No .epi file downloads
4. Installation errors
5. Cell execution errors (red text)

### ⚠️ Warning Signs:
1. Download size is < 10 KB (file may be corrupted)
2. Viewer doesn't load (shows blank area)
3. Timeline has fewer than 7 steps
4. Any cell takes > 30 seconds to run

---

## 📱 Mobile/Tablet Test (Optional but Recommended)

- [ ] Open Colab on tablet/phone
- [ ] Run the notebook
- [ ] Check if viewer is readable on small screen
- [ ] Verify download works on mobile

**Note**: Some investors might view on iPad during meetings!

---

## 🎯 Before Sharing with Investors

### Final Prep Checklist:
- [ ] Run through entire notebook one more time
- [ ] Clear ALL outputs: **Edit → Clear all outputs**
- [ ] Save the notebook
- [ ] Download .ipynb file from Colab
- [ ] Upload to a clean Google Drive folder
- [ ] Set sharing to "Anyone with link can view"
- [ ] Test the share link in incognito mode
- [ ] Copy link to send to investors

---

## 📧 Sample Email to Investors

```
Subject: EPI Live Demo - Cryptographic AI Compliance

Hi [Investor Name],

As discussed, here's the live demo of our cryptographic AI compliance system.

📎 Demo Link: [Your Colab link]

⏱️ Takes 60 seconds to run
🎯 Shows cryptographic proof of AI decisions
🛡️ Includes tamper-detection demo

Instructions:
1. Click the link (opens in Google Colab)
2. Click: Runtime → Run all
3. Watch the magic happen

The demo will:
- Record a live AI trading decision
- Download cryptographic proof to your machine
- Verify the signature (Ed25519)
- Show you can't fake the evidence

Looking forward to discussing this further.

Best,
[Your Name]
mohdibrahim@epilabs.org
epilabs.org
```

---

## 🐛 Troubleshooting Common Issues

### Issue: "Module not found: epi-recorder"
**Fix**: Restart runtime and run again. Colab sometimes needs a clean start.

### Issue: No file downloads
**Fix**: Check browser permissions. Chrome may block downloads from Colab.

### Issue: Viewer shows "UNSIGNED"
**Fix**: Check that `auto_sign=True` is in the recording code. Should be on line with `with record(...)`.

### Issue: Tamper test doesn't fail
**Fix**: This is a bug. DO NOT show to investors. The `epi verify` command should detect the tampering.

---

## 📊 Success Metrics

After showing to investors, track:
- [ ] Demo completed without errors
- [ ] Investor understood the value proposition
- [ ] Investor asked follow-up questions (good sign!)
- [ ] Investor requested technical deep-dive (very good sign!)
- [ ] Schedule next meeting

---

## 🎬 Demo Day Protocol

1. **30 min before**: Run full test in private
2. **15 min before**: Clear all outputs
3. **5 min before**: Test share link in incognito
4. **During demo**: Share screen, run live
5. **After demo**: Ask for feedback

---

**Last Updated**: 2025-12-22  
**Version**: v2.1.1  
**Status**: ✅ READY FOR INVESTORS (after testing!)

---

## 📞 Emergency Contacts

If demo breaks during investor meeting:
- **Backup plan**: Show website simulator at epilabs.org
- **Escalation**: Have GitHub repo open (shows working code)
- **Recovery**: "Let me share pre-recorded version" (have video ready)

**Remember**: Live demo issues happen. Investors understand. What matters is how you handle it!
