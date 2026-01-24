"""
Script to intentionally tamper with an .epi file to test verification failure.
"""
import zipfile
import json
import shutil
import os
from pathlib import Path

def tamper_epi(epi_path):
    print(f"Tampering with {epi_path}...")
    temp_dir = Path("tamper_temp")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()

    # 1. Unzip
    with zipfile.ZipFile(epi_path, 'r') as z:
        z.extractall(temp_dir)
    
    # 2. Modify steps.jsonl (The Crime)
    steps_path = temp_dir / "steps.jsonl"
    with open(steps_path, 'a') as f:
        f.write('{"index": 999, "kind": "fake.event", "content": "I hacked this file"}\n')
    print("   [CRIME] Added fake step to steps.jsonl")

    # 3. Zip it back (The Cover-up)
    # create_archive adds the suffix, so we strip it from base_name
    shutil.make_archive(str(epi_path).replace('.epi', ''), 'zip', temp_dir)
    
    # Rename .zip back to .epi
    shutil.move(str(epi_path).replace('.epi', '.zip'), epi_path)
    
    # Cleanup
    shutil.rmtree(temp_dir)
    print("   [DONE] File tampered and repackaged.")

if __name__ == "__main__":
    # Find the investor demo file
    recordings = list(Path("epi-recordings").glob("*.epi"))
    if not recordings:
        print("No recordings found!")
        exit(1)
        
    # Pick the latest
    target = sorted(recordings, key=os.path.getmtime)[-1]
    tamper_epi(target)
    print(f"TARGET_FILE={target}")
