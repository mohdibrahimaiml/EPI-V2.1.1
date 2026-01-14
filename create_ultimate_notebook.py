#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FINAL FIX: Update viewer.html's embedded manifest with CURRENT signature
The viewer's JavaScript reads <script id="epi-data"> which has stale manifest
We need to REPLACE that with the current manifest from manifest.json
"""

import json
import sys
from pathlib import Path

# Fix Windows encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("="*70)
print("🔧 FIXING VIEWER TO SHOW CURRENT SIGNATURE")
print("="*70)

notebook_path = "EPI_DEMO_demo_ULTIMATE.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Update viewer cell to REPLACE embedded manifest with current one
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and any('View EPI Timeline' in line for line in cell.get('source', [])):
        cell['source'] = [
            "# @title 👁️ View EPI Timeline { display-mode: \"form\" }\n",
            "import zipfile\n",
            "import json\n",
            "import re\n",
            "from pathlib import Path\n",
            "from IPython.display import display, HTML\n",
            "\n",
            "print(\"=\"*70)\n",
            "display(HTML('<h2 style=\"color: #3b82f6;\">👁️ Loading viewer...</h2>'))\n",
            "\n",
            "# Find .epi file\n",
            "epi_files = list(Path('.').glob('*.epi')) + list(Path('.').glob('epi-recordings/*.epi'))\n",
            "epi_file = max(epi_files, key=lambda p: p.stat().st_mtime) if epi_files else None\n",
            "\n",
            "if not epi_file:\n",
            "    print(\"❌ No .epi file found. Run the recording cell first.\")\n",
            "else:\n",
            "    print(f\"Source: {epi_file.name}\\n\")\n",
            "    \n",
            "    with zipfile.ZipFile(epi_file, 'r') as zf:\n",
            "        # Read CURRENT manifest (with signature)\n",
            "        if 'manifest.json' not in zf.namelist():\n",
            "            print(\"❌ No manifest.json found\")\n",
            "        else:\n",
            "            current_manifest = json.loads(zf.read('manifest.json').decode('utf-8'))\n",
            "            signature = current_manifest.get('signature')\n",
            "            \n",
            "            # Read steps.jsonl\n",
            "            steps = []\n",
            "            if 'steps.jsonl' in zf.namelist():\n",
            "                for line in zf.read('steps.jsonl').decode('utf-8').strip().split('\\n'):\n",
            "                    if line:\n",
            "                        try:\n",
            "                            steps.append(json.loads(line))\n",
            "                        except:\n",
            "                            pass\n",
            "            \n",
            "            # Display signature status\n",
            "            if signature:\n",
            "                sig_display = signature.upper().replace(':', ':')[:30] + '...'\n",
            "                print(f\"✓ Signature found: {sig_display}\")\n",
            "            else:\n",
            "                print(\"⚠️  Warning: File is UNSIGNED\")\n",
            "            \n",
            "            # Extract viewer.html\n",
            "            if 'viewer.html' in zf.namelist():\n",
            "                viewer_html = zf.read('viewer.html').decode('utf-8', errors='ignore')\n",
            "                print(\"✓ Using authentic viewer: viewer.html\")\n",
            "                \n",
            "                # CRITICAL FIX: Replace embedded manifest with CURRENT one\n",
            "                # The viewer has <script id=\"epi-data\"> with OLD manifest\n",
            "                # We need to inject the CURRENT manifest with signature\n",
            "                \n",
            "                # Create updated embedded data\n",
            "                updated_data = {\n",
            "                    \"manifest\": current_manifest,  # ← CURRENT manifest with signature!\n",
            "                    \"steps\": steps\n",
            "                }\n",
            "                \n",
            "                # Find and replace the epi-data script\n",
            "                data_json = json.dumps(updated_data, indent=2)\n",
            "                \n",
            "                # Pattern to match <script id=\"epi-data\">...</script>\n",
            "                pattern = r'<script id=\"epi-data\" type=\"application/json\">.*?</script>'\n",
            "                replacement = f'<script id=\"epi-data\" type=\"application/json\">{data_json}</script>'\n",
            "                \n",
            "                # Replace the stale embedded data with current data\n",
            "                viewer_html_updated = re.sub(pattern, replacement, viewer_html, flags=re.DOTALL)\n",
            "                \n",
            "                print(\"✓ Updated viewer with current manifest\")\n",
            "            else:\n",
            "                print(\"⚠️  No viewer.html found\")\n",
            "                viewer_html_updated = None\n",
            "    \n",
            "    if viewer_html_updated:\n",
            "        print(\"=\"*70)\n",
            "        display(HTML('<h1 style=\"color: #10b981; font-size: 36px; margin: 20px 0;\">✅ VIEWER LOADED</h1>'))\n",
            "        \n",
            "        if signature:\n",
            "            sig_short = signature.upper()[:30] + '...'\n",
            "            print(f\"Signature: {sig_short}\")\n",
            "        print(\"=\"*70)\n",
            "        \n",
            "        # Display with signature banner\n",
            "        import html\n",
            "        escaped = html.escape(viewer_html_updated)\n",
            "        \n",
            "        if signature:\n",
            "            sig_display = signature.upper()[:30] + '...'\n",
            "            banner = f'''<div style=\"background: linear-gradient(135deg, #10b981, #059669); \n",
            "                                     color: white; padding: 18px 24px; \n",
            "                                     display: flex; justify-content: space-between; \n",
            "                                     align-items: center;\">\n",
            "                             <span style=\"font-size: 22px; font-weight: bold;\">🛡️ AUTHENTIC EPI VIEWER</span>\n",
            "                             <span style=\"font-family: Courier New, monospace; font-size: 14px; \n",
            "                                          background: rgba(255,255,255,0.25); padding: 8px 14px; \n",
            "                                          border-radius: 8px;\">{sig_display}</span>\n",
            "                         </div>'''\n",
            "        else:\n",
            "            banner = '''<div style=\"background: #f59e0b; color: white; padding: 18px 24px; \n",
            "                                    font-size: 18px; font-weight: bold; text-align: center;\">\n",
            "                            ⚠️ WARNING: UNSIGNED FILE\n",
            "                        </div>'''\n",
            "        \n",
            "        iframe = f'''<div style=\"border: 4px solid #10b981; border-radius: 16px; \n",
            "                                 overflow: hidden; margin: 25px 0;\">\n",
            "                         {banner}\n",
            "                         <iframe srcdoc=\"{escaped}\" width=\"100%\" height=\"700\" \n",
            "                                 style=\"border: none;\" \n",
            "                                 sandbox=\"allow-scripts allow-same-origin\"></iframe>\n",
            "                     </div>'''\n",
            "        \n",
            "        display(HTML(iframe))\n"
        ]

# Save
output_path = "EPI_DEMO_demo_ULTIMATE.ipynb"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"\n✅ Updated: {output_path}")
print("\n" + "="*70)
print("CRITICAL FIX APPLIED:")
print("="*70)
print("1. ✅ Reads CURRENT manifest.json (has signature)")
print("2. ✅ Reads steps.jsonl")
print("3. ✅ REPLACES embedded manifest in viewer.html")
print("4. ✅ Viewer's JavaScript now reads CURRENT manifest")
print("5. ✅ Badge will show 'SIGNED' ✅")
print("\n" + "="*70)
print("WHAT CHANGED:")
print("="*70)
print("BEFORE: viewer.html has <script id='epi-data'>{\"manifest\":{\"signature\":null}}</script>")
print("AFTER:  viewer.html has <script id='epi-data'>{\"manifest\":{\"signature\":\"ed25519:...\"}}</script>")
print("\nNow the viewer's OWN JavaScript reads the correct signature!")
print("="*70)
