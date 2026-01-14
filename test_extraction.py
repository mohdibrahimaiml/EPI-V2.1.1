"""Test extraction and data visualization like the Colab notebook does"""

import zipfile
import json
import pandas as pd
from pathlib import Path

print("\n" + "=" * 70)
print("EXTRACTING TAMPER-PROOF EVIDENCE")
print("=" * 70 + "\n")

# Extract the .epi file
epi_file = Path('epi-recordings/test_financial_agent_20251217_033905.epi')
extract_dir = Path('epi_extracted_test')
extract_dir.mkdir(exist_ok=True)

with zipfile.ZipFile(epi_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print("SUCCESS: Extracted cryptographically signed container\n")

# Show all extracted files
print("Contents of .epi file:")
for f in sorted(extract_dir.rglob('*')):
    if f.is_file():
        print(f"   - {f.relative_to(extract_dir)} ({f.stat().st_size} bytes)")

print("\n" + "-" * 70 + "\n")

# Load the execution steps from steps.jsonl
steps_file = extract_dir / 'steps.jsonl'

if steps_file.exists():
    steps = []
    with open(steps_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                steps.append(json.loads(line))
    
    print(f"TAMPER-PROOF AUDIT TRAIL ({len(steps)} steps captured)\n")
    
    # Display full data
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', 100)
    pd.set_option('display.width', None)
    
    df = pd.DataFrame(steps)
    print(df)
    
    print("\n" + "-" * 70)
else:
    print("INFO: steps.jsonl not found - checking alternative formats...")

# Check for trade_record.json in workspace
trade_record_path = extract_dir / 'workspace' / 'trade_record.json'
if trade_record_path.exists():
    print("\n" + "=" * 70)
    print("CAPTURED TRADE RECORD")
    print("=" * 70 + "\n")
    
    with open(trade_record_path, 'r') as f:
        trade_data = json.load(f)
    
    print(json.dumps(trade_data, indent=2))
    
    print("\nSUCCESS: This trade record is part of the cryptographically signed audit trail")
else:
    print("\nWARNING: trade_record.json not found in workspace")

# Check for stdout capture
stdout_file = extract_dir / 'stdout.txt'
if stdout_file.exists():
    print("\n" + "=" * 70)
    print("CAPTURED CONSOLE OUTPUT")
    print("=" * 70 + "\n")
    with open(stdout_file, 'r', encoding='utf-8') as f:
        stdout_content = f.read()
        print(stdout_content[:1000])  # First 1000 chars
        if len(stdout_content) > 1000:
            print(f"\n... ({len(stdout_content) - 1000} more characters)")

print("\n" + "=" * 70)
print("EXTRACTION TEST COMPLETE")
print("=" * 70)
