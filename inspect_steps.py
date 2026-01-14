
import glob
import os
import zipfile
import json
import codecs
from pathlib import Path
import sys

# Force UTF-8 for Windows console
sys.stdout.reconfigure(encoding='utf-8')

print("🔍 Searching for .epi files...")

# Recursive search
search_patterns = ['*.epi', 'epi-recordings/*.epi', '**/*.epi']
epi_files = []
for pattern in search_patterns:
    epi_files.extend(list(Path('.').glob(pattern)))

if not epi_files:
    print("❌ No .epi files found anywhere.")
    exit(1)

# Sort by modification time
latest_epi = max(epi_files, key=os.path.getmtime)
print(f"📂 Found latest file: {latest_epi}")
print(f"   Size: {latest_epi.stat().st_size} bytes")

try:
    with zipfile.ZipFile(latest_epi, 'r') as z:
        if 'steps.jsonl' in z.namelist():
            print("   Reading steps.jsonl...")
            raw_steps = z.read('steps.jsonl').decode('utf-8')
            lines = [l for l in raw_steps.splitlines() if l.strip()]
            
            print(f"✅ Found {len(lines)} lines of data.")
            
            if len(lines) == 0:
                print("⚠️ FILE IS EMPTY! The recorder did not capture any steps.")
            else:
                steps = []
                for i, line in enumerate(lines):
                    try:
                        steps.append(json.loads(line))
                    except json.JSONDecodeError:
                        print(f"❌ JSON Error on line {i+1}")
                
                print(f"✅ Successfully parsed {len(steps)} JSON objects.")
                if len(steps) > 0:
                    print(f"   First Step: {steps[0].get('kind')} - {steps[0].get('timestamp')}")
                    # Check for 'content'
                    if 'content' not in steps[0]:
                        print("⚠️ First step missing 'content' field!")
        else:
            print("❌ steps.jsonl MISSING from archive.")

except Exception as e:
    print(f"❌ Error reading file: {e}")
