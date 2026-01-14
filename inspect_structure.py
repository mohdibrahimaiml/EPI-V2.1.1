import zipfile
import json
from pathlib import Path

print("=" * 70)
print("INSPECTING .epi FILE STRUCTURE")
print("=" * 70)

# Use an existing .epi file from epi-recordings
epi_file = Path(r"C:\Users\dell\epi-recorder\epi-recordings\demo_20251215_163202.epi")

print(f"\nFile: {epi_file.name}")
print(f"Size: {epi_file.stat().st_size / 1024:.2f} KB\n")

# Open and inspect
with zipfile.ZipFile(epi_file, 'r') as z:
    files = z.namelist()
    print("CONTENTS:")
    print("-" * 70)
    for f in sorted(files):
        info = z.getinfo(f)
        size = info.file_size
        print(f"  {f:<40} {size:>10} bytes")
    
    print("\n" + "=" * 70)
    print("STRUCTURE VERIFICATION")
    print("=" * 70)
    
    # Expected structure from user
    checks = {
        "mimetype": "mimetype" in files,
        "manifest.json": "manifest.json" in files,
        "steps.jsonl": "steps.jsonl" in files,
        "env.json (or environment.json)": "env.json" in files or "environment.json" in files,
        "artifacts/ folder": any(f.startswith("artifacts/") for f in files),
        "viewer/ folder": any(f.startswith("viewer/") or f.startswith("viewer.html") or "index.html" in f for f in files),
    }
    
    print("\nREQUIRED COMPONENTS:")
    for component, present in checks.items():
        status = "YES" if present else "NO"
        print(f"  [{status}] {component}")
    
    # Check mimetype content
    if "mimetype" in files:
        mimetype = z.read("mimetype").decode('utf-8').strip()
        print(f"\nMIMETYPE: '{mimetype}'")
        expected = "application/epi+zip"
        if mimetype == expected:
            print(f"  YES - matches '{expected}'")
        else:
            print(f"  NO - expected '{expected}'")
    
    # Check steps.jsonl
    if "steps.jsonl" in files:
        steps_content = z.read("steps.jsonl").decode('utf-8')
        lines = [l for l in steps_content.split('\n') if l.strip()]
        print(f"\nSTEPS.JSONL: {len(lines)} entries")
        if len(lines) > 0:
            first = json.loads(lines[0])
            print(f"  First: {first.get('kind', 'N/A')}")
            if len(lines) > 1:
                last = json.loads(lines[-1])
                print(f"  Last: {last.get('kind', 'N/A')}")

print("\n" + "=" * 70)
print("FINAL VERDICT")
print("=" * 70)

all_present = all(checks.values())
if all_present:
    print("\nYES - Demo follows the expected structure!")
else:
    missing = [k for k, v in checks.items() if not v]
    print(f"\nNO - Missing: {', '.join(missing)}")

print("=" * 70)
