# 📍 WHERE YOU'LL SEE "SIGNED" STATUS

When you run the notebook in Colab, you'll see the signature in **3 locations**:

---

## 1️⃣ In the Demo Cell Output (RIGHT AFTER RECORDING)

After the "🏦 FINANCIAL AI - EXECUTING TRADE" section completes, you'll see:

```
✓ FILE IS SIGNED: ed25519:default:eGMuh2Cze0WgJy2QW+vXh+/D...

======================================================================
✅ EVIDENCE CREATED
======================================================================
📁 File: trade_evidence.epi
💾 Size: 13.9 KB
⏱️  Time: 4.6s
🔐 Cryptographically signed with Ed25519

======================================================================
```

**Look for this line:**
```
✓ FILE IS SIGNED: ed25519:default:eGMuh2Cze0Wg...
```

If you see this ↑, the signature worked!

❌ **If you see this instead:**
```
❌ CRITICAL ERROR: FILE IS UNSIGNED!
```
→ Something went wrong. Don't show to investors yet.

---

## 2️⃣ In the Viewer Cell - TOP BANNER

When you run the viewer cell (third cell), you'll see a **green banner** at the very top of the viewer:

```
┌─────────────────────────────────────────────────────────────┐
│ 🛡️ AUTHENTIC EPI VIEWER    ED25519:DEFAULT:eGMuh2Cze0Wg... │  ← GREEN BANNER
└─────────────────────────────────────────────────────────────┘
```

**Visual:**
```
╔═══════════════════════════════════════════════════════════════════╗
║ GREEN BACKGROUND                                                  ║
║ 🛡️ AUTHENTIC EPI VIEWER          ED25519:DEFAULT:eGMuh2Cze0Wg... ║
╚═══════════════════════════════════════════════════════════════════╝
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│  EPI Viewer                                                       │
│  Evidence Packaged Infrastructure for AI Workflows                │
│                                                                   │
│  [Your timeline content here...]                                 │
└───────────────────────────────────────────────────────────────────┘
```

This banner is **impossible to miss** - it's at the very top of the viewer iframe!

---

## 3️⃣ In the Viewer - TOP RIGHT BADGE

In the upper right corner of the viewer, **inside the viewer interface itself**, you'll see a badge:

```
EPI Viewer                                          ┌─────────┐
Evidence Packaged Infrastructure                   │ ✓ Signed │  ← GREEN BADGE
                                                     └─────────┘
```

**Visual:**
```
┌──────────────────────────────────────────────────────────────┐
│ EPI Viewer                                    ╔═══════════╗  │
│ Evidence Packaged Infrastructure              ║ ✓ Signed  ║  │ ← GREEN
│                                                ╚═══════════╝  │
│                                                                │
│ Manifest:                    Timeline:                        │
│ - Workflow ID                - Step 1: MARKET_DATA            │
│ - Created: ...               - Step 2: TECHNICAL              │
└──────────────────────────────────────────────────────────────┘
```

**What the badge looks like:**

✅ **Signed** (Green background, green text)  
⚠️ **Unsigned** (Yellow/Orange background, dark text) ← BAD, don't show!

---

## 📸 Screenshot Guide

Here's what to look for:

### ✅ CORRECT (SIGNED):

**Demo Cell:**
```
✓ FILE IS SIGNED: ed25519:default:eGMuh2Cze0WgJy...
🔐 Cryptographically signed with Ed25519
```

**Viewer Banner:**
```
[GREEN BAR] 🛡️ AUTHENTIC EPI VIEWER    ED25519:DEFAULT:eGMuh2...
```

**Viewer Badge:**
```
[GREEN BADGE] ✓ Signed
```

---

### ❌ WRONG (UNSIGNED):

**Demo Cell:**
```
❌ CRITICAL ERROR: FILE IS UNSIGNED!
This demo requires auto_sign=True to work properly.
```

**Viewer Banner:**
```
[YELLOW/ORANGE BAR] ⚠️ WARNING: UNSIGNED FILE
```

**Viewer Badge:**
```
[YELLOW BADGE] ⚠ Unsigned
```

---

## 🎯 Quick Visual Check

When you run the notebook, do this:

1. **Scroll to demo cell output** → Look for green "✓ FILE IS SIGNED"
2. **Scroll to viewer cell** → Look for green banner at top
3. **Look at viewer top-right** → Look for green "Signed" badge

If all 3 are ✅ GREEN → You're good to show investors!

If ANY are ❌ RED/YELLOW → Don't show yet, fix the issue first

---

## 🖼️ Mock-up of What You'll See

```
╔═══════════════════════════════════════════════════════════════╗
║                     COLAB NOTEBOOK                             ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║ [Cell 1: Demo Cell]                                           ║
║                                                                ║
║ ✓ FILE IS SIGNED: ed25519:default:eGMuh2Cze0WgJy...     ✅    ║
║ ✅ EVIDENCE CREATED                                            ║
║ 📁 File: trade_evidence.epi                                   ║
║ 🔐 Cryptographically signed with Ed25519                      ║
║                                                                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║ [Cell 2: Verify Cell]                                         ║
║                                                                ║
║ [Shows verification output...]                                ║
║                                                                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║ [Cell 3: Viewer Cell]                                         ║
║                                                                ║
║ ✅ VIEWER LOADED                                               ║
║ Signature: ED25519:DEFAULT:eGMuh2Cze0Wg...                    ║
║                                                                ║
║ ┌─────────────────────────────────────────────────────────┐  ║
║ │ [GREEN] 🛡️ AUTHENTIC EPI VIEWER    ED25519:DEFAULT:... │ ✅ ║
║ ├─────────────────────────────────────────────────────────┤  ║
║ │                                                         │  ║
║ │ EPI Viewer                           [GREEN] ✓ Signed  │ ✅ ║
║ │                                                         │  ║
║ │ [Viewer content with timeline...]                      │  ║
║ │                                                         │  ║
║ └─────────────────────────────────────────────────────────┘  ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📋 Investor Demo Checklist

Before showing to investors, verify these 3 things:

- [ ] **Demo cell output** shows: "✓ FILE IS SIGNED"
- [ ] **Viewer banner** is GREEN with signature hash
- [ ] **Viewer badge** says "Signed" in GREEN

If all 3 are ✅ → Demo is ready!

---

## 🎬 What To Point Out During Demo

**After demo cell runs:**
> "See that? 'FILE IS SIGNED' with the Ed25519 signature hash.  
> This was generated in real-time, right now."

**When viewer loads:**
> "Notice the green banner at the top - that's the cryptographic  
> signature. And in the upper right, you see the 'Signed' badge.  
> This proves the entire timeline is verified."

**During tamper test:**
> "Watch what happens when we try to fake the evidence...  
> [Run tamper cell]  
> The verification fails. The signature makes it impossible to forge."

---

## 💡 Pro Tip

**Take a screenshot** when all 3 show "SIGNED" and save it for your pitch deck!

Use it as proof that the system works.

---

**Summary:**

You'll see "SIGNED" in **3 places**:
1. Demo cell output: `✓ FILE IS SIGNED: ed25519...`
2. Viewer top banner: Green bar with signature
3. Viewer badge: Green "✓ Signed" in top-right

All 3 must be GREEN for investor demo! ✅
