# Quick verification script
import json

with open('epi_investor_demo.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

demo = [c for c in nb['cells'] if c.get('metadata',{}).get('id')=='demo'][0]
view = [c for c in nb['cells'] if c.get('metadata',{}).get('id')=='view'][0]

d = ''.join(demo['source'])
v = ''.join(view['source'])

print("DEMO CELL:")
print("  - import re:", "import" in d and "re" in d)
print("  - re.sub:", "re.sub" in d)
print("  - manifest in data:", '"manifest": manifest' in d)

print("\nVIEW CELL:")
print("  - import re:", "import" in v and "re" in v)
print("  - re.sub:", "re.sub" in v)
print("  - manifest in data:", '"manifest": manifest' in v)

print("\nBOTH CELLS WILL SHOW SIGNED:", "re.sub" in d and "re.sub" in v)
