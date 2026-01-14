# Verify the notebook changes
import json

with open('epi_investor_demo.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

demo = [c for c in nb['cells'] if c.get('metadata',{}).get('id')=='demo'][0]
src = ''.join(demo['source'])

print("Verification Results:")
print("-" * 50)
if 'SEC_Evidence_Viewer.html' in src:
    print("[OK] Viewer HTML extraction: PRESENT")
else:
    print("[FAIL] Viewer HTML extraction: MISSING")

if 'files.download(str(viewer_html_file))' in src:
    print("[OK] Dual download logic: PRESENT")
else:
    print("[FAIL] Dual download logic: MISSING")

if 'DOWNLOADING 2 FILES' in src:
    print("[OK] Updated messaging: PRESENT")
else:
    print("[FAIL] Updated messaging: MISSING")

print("-" * 50)
print("Demo cell preview (download section):")
idx = src.find("# EXTRACT VIEWER")
if idx != -1:
    print(src[idx:idx+500])
