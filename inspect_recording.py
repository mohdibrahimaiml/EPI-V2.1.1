
import glob
import os
import zipfile
import json
from pathlib import Path

# Find newest .epi file
epi_files = list(Path('.').glob('*.epi'))
if not epi_files:
    print("❌ No .epi files found in current directory.")
    exit(1)

latest_epi = max(epi_files, key=os.path.getmtime)
print(f"🔍 Inspecting: {latest_epi.name}")
print(f"   Size: {latest_epi.stat().st_size} bytes")

try:
    with zipfile.ZipFile(latest_epi, 'r') as z:
        # Check integrity
        print(f"   Files in archive: {z.namelist()}")
        
        if 'steps.jsonl' in z.namelist():
            raw_steps = z.read('steps.jsonl').decode('utf-8')
            steps = [json.loads(line) for line in raw_steps.splitlines() if line]
            print(f"✅ Found {len(steps)} steps.")
            
            if len(steps) > 0:
                print("   First step:", json.dumps(steps[0], indent=2))
                print("   Last step:", json.dumps(steps[-1], indent=2))
            else:
                print("⚠️ steps.jsonl is EMPTY.")
        else:
            print("❌ steps.jsonl MISSING from archive.")
            
        if 'viewer.html' in z.namelist():
            print("✅ viewer.html is present.")
        else:
            print("⚠️ viewer.html is MISSING.")

except Exception as e:
    print(f"❌ Error reading file: {e}")
