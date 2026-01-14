#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diagnose why the EPI file is unsigned and fix it
"""

import sys
import os
import subprocess
import json
import zipfile
from pathlib import Path

# Fix Windows encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("=" * 70)
print("🔍 DIAGNOSING EPI SIGNING ISSUE")
print("=" * 70)

# Step 1: Check if epi-recorder is installed
print("\n1️⃣ Checking epi-recorder installation...")
try:
    result = subprocess.run([sys.executable, '-m', 'pip', 'show', 'epi-recorder'], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ epi-recorder is installed")
        # Extract version
        for line in result.stdout.split('\n'):
            if line.startswith('Version:'):
                print(f"   Version: {line.split(':')[1].strip()}")
    else:
        print("❌ epi-recorder is NOT installed")
        print("   Installing now...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'epi-recorder'], check=True)
        print("✅ Installed epi-recorder")
except Exception as e:
    print(f"❌ Error checking installation: {e}")

# Step 2: Check if signing keys exist
print("\n2️⃣ Checking for signing keys...")
epi_config_dir = Path.home() / '.epi'
keys_dir = epi_config_dir / 'keys'

if keys_dir.exists():
    print(f"✅ Keys directory exists: {keys_dir}")
    key_files = list(keys_dir.glob('*.key'))
    if key_files:
        print(f"   Found {len(key_files)} key file(s):")
        for key_file in key_files:
            print(f"   - {key_file.name}")
    else:
        print("⚠️  Keys directory exists but is empty")
else:
    print("❌ No keys directory found")
    print(f"   Expected location: {keys_dir}")

# Step 3: Try to initialize signing
print("\n3️⃣ Initializing signing system...")
try:
    # Check if epi command works
    result = subprocess.run(['epi', 'keygen', '--help'], 
                          capture_output=True, text=True, timeout=5)
    if result.returncode == 0:
        print("✅ EPI command line tool is available")
        
        # Try to generate a default key if it doesn't exist
        print("\n4️⃣ Ensuring default signing key exists...")
        result = subprocess.run(['epi', 'keygen', 'default'], 
                              capture_output=True, text=True, timeout=10)
        
        if 'already exists' in result.stdout or 'already exists' in result.stderr:
            print("✅ Default key already exists")
        elif result.returncode == 0:
            print("✅ Created default signing key")
        else:
            print(f"⚠️  Key generation output: {result.stdout}")
            if result.stderr:
                print(f"   Stderr: {result.stderr}")
    else:
        print("⚠️  EPI CLI not working properly")
        print(f"   Output: {result.stdout}")
        print(f"   Error: {result.stderr}")
        
except subprocess.TimeoutExpired:
    print("⚠️  Command timed out")
except FileNotFoundError:
    print("❌ 'epi' command not found in PATH")
    print("   This might be a Colab-specific issue")
except Exception as e:
    print(f"⚠️  Error: {e}")

# Step 5: Test actual recording with auto_sign
print("\n5️⃣ Testing signature generation...")
test_script = '''
import sys
from pathlib import Path
import time

try:
    from epi_recorder import record
    
    print("Creating test recording with auto_sign=True...")
    with record("test_signature.epi", workflow_name="Signature Test", auto_sign=True) as epi:
        epi.log_step("TEST", {"message": "Testing signature", "timestamp": time.time()})
    
    # Check if file was created
    test_file = Path("test_signature.epi")
    if test_file.exists():
        print(f"✅ Test file created: {test_file.stat().st_size} bytes")
        
        # Check signature
        import zipfile, json
        with zipfile.ZipFile(test_file, 'r') as z:
            if 'manifest.json' in z.namelist():
                manifest = json.loads(z.read('manifest.json').decode('utf-8'))
                sig = manifest.get('signature')
                
                if sig:
                    print(f"✅ SIGNATURE FOUND: {sig[:50]}...")
                    print("   Signature algorithm:", sig.split(':')[0] if ':' in sig else 'unknown')
                else:
                    print("❌ NO SIGNATURE in manifest")
                    print("   Manifest keys:", list(manifest.keys()))
                    print("   auto_sign=True was specified but signature is NULL")
            else:
                print("❌ No manifest.json in .epi file")
        
        # Cleanup
        test_file.unlink()
    else:
        print("❌ Test file was not created")
        
except ImportError as e:
    print(f"❌ Cannot import epi_recorder: {e}")
except Exception as e:
    print(f"❌ Error during test: {e}")
    import traceback
    traceback.print_exc()
'''

# Write and run test script
test_path = Path('test_signing.py')
with open(test_path, 'w', encoding='utf-8') as f:
    f.write(test_script)

try:
    result = subprocess.run([sys.executable, str(test_path)], 
                          capture_output=True, text=True, timeout=30)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
finally:
    test_path.unlink(missing_ok=True)

# Step 6: Provide fix recommendations
print("\n" + "=" * 70)
print("📋 DIAGNOSIS SUMMARY")
print("=" * 70)

print("\nIf signature is STILL NULL, the issue is likely:")
print("1. epi-recorder package needs signing keys initialized")
print("2. Need to run 'epi keygen default' first")
print("3. Python API auto_sign may have a bug")

print("\n" + "=" * 70)
print("🔧 RECOMMENDED FIX")
print("=" * 70)

print("""
For Google Colab, add this to the FIRST cell of your notebook:

```python
# Initialize EPI signing (run once per session)
import subprocess
import sys

# Install epi-recorder
!pip install -q --upgrade epi-recorder

# Generate signing key
result = subprocess.run(['epi', 'keygen', 'default'], 
                       capture_output=True, text=True)
if 'created' in result.stdout or 'exists' in result.stdout:
    print("✅ Signing key ready")
else:
    print("❌ Key generation failed:", result.stdout)

# Verify it works
from epi_recorder import record
import time

# Quick test
with record("_test.epi", workflow_name="test", auto_sign=True) as epi:
    epi.log_step("TEST", {"time": time.time()})

import zipfile, json
from pathlib import Path

test_file = Path("_test.epi")
with zipfile.ZipFile(test_file, 'r') as z:
    m = json.loads(z.read('manifest.json'))
    if m.get('signature'):
        print("✅ AUTO-SIGN WORKING!")
    else:
        print("❌ AUTO-SIGN FAILED - Manual signing needed")
        
test_file.unlink()
```
""")

print("\n" + "=" * 70)
print("Alternative: Use manual signing")
print("=" * 70)

print("""
If auto_sign doesn't work, use this in your demo cell:

```python
# After recording
epi_file = Path("trade_evidence.epi")

# Sign manually
subprocess.run(['epi', 'sign', str(epi_file), '--key', 'default'], check=True)

# Verify it's signed
result = subprocess.run(['epi', 'verify', str(epi_file)], 
                       capture_output=True, text=True)
if 'Trust Level: HIGH' in result.stdout:
    print("✅ File signed successfully")
```
""")

print("\n" + "=" * 70)
