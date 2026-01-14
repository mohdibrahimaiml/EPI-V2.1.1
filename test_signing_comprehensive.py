#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPREHENSIVE TEST: Verify EPI signing works in practice
This mimics exactly what the notebook does
"""

import sys
import os
from pathlib import Path
import zipfile
import json
import time
import subprocess

# Fix Windows encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("="*70)
print("🧪 COMPREHENSIVE EPI SIGNING TEST")
print("="*70)
print("\nThis test mimics the exact notebook flow to verify signing works.\n")

# Test 1: Check epi-recorder installation
print("TEST 1: Checking epi-recorder installation")
print("-"*70)
try:
    from epi_recorder import record
    print("✅ epi-recorder imported successfully")
except ImportError as e:
    print(f"❌ Cannot import epi-recorder: {e}")
    sys.exit(1)

# Test 2: Check if keys exist
print("\nTEST 2: Checking for signing keys")
print("-"*70)
keys_dir = Path.home() / '.epi' / 'keys'
if keys_dir.exists():
    key_files = list(keys_dir.glob('*.key'))
    print(f"✅ Keys directory exists: {keys_dir}")
    print(f"   Found {len(key_files)} key file(s)")
    if key_files:
        for kf in key_files[:5]:  # Show first 5
            print(f"   - {kf.name}")
else:
    print(f"⚠️  No keys directory at {keys_dir}")
    print("   Will try to create keys during test...")

# Test 3: Try auto_sign=True (like the notebook)
print("\nTEST 3: Testing auto_sign=True (Primary method)")
print("-"*70)
test_file_1 = Path("test_auto_sign_method1.epi")
try:
    print("Creating recording with auto_sign=True...")
    
    with record(str(test_file_1), workflow_name="Auto Sign Test", auto_sign=True) as epi:
        epi.log_step("MARKET_DATA", {"symbol": "AAPL", "price": 185.43})
        epi.log_step("TECHNICAL", {"indicator": "50-Day MA", "signal": "BULLISH"})
        time.sleep(0.1)
    
    # Check if file exists
    if test_file_1.exists():
        print(f"✅ File created: {test_file_1} ({test_file_1.stat().st_size} bytes)")
        
        # Check signature
        with zipfile.ZipFile(test_file_1, 'r') as z:
            if 'manifest.json' in z.namelist():
                manifest = json.loads(z.read('manifest.json').decode('utf-8'))
                sig = manifest.get('signature')
                
                if sig:
                    print(f"✅ SIGNATURE FOUND (auto_sign=True): {sig[:60]}...")
                    auto_sign_works = True
                else:
                    print("❌ NO SIGNATURE despite auto_sign=True")
                    print(f"   Manifest keys: {list(manifest.keys())}")
                    auto_sign_works = False
    else:
        print("❌ File was not created")
        auto_sign_works = False
        
except Exception as e:
    print(f"❌ Error during auto_sign test: {e}")
    import traceback
    traceback.print_exc()
    auto_sign_works = False

# Test 4: Try manual signing (backup method)
print("\nTEST 4: Testing manual signing (Backup method)")
print("-"*70)
test_file_2 = Path("test_manual_sign_method2.epi")
try:
    # Create file WITHOUT auto_sign (or pretend it failed)
    print("Creating recording without signature...")
    
    with record(str(test_file_2), workflow_name="Manual Sign Test", auto_sign=False) as epi:
        epi.log_step("TEST", {"message": "testing manual signing"})
        time.sleep(0.1)
    
    if test_file_2.exists():
        print(f"✅ Unsigned file created: {test_file_2}")
        
        # Verify it's unsigned
        with zipfile.ZipFile(test_file_2, 'r') as z:
            manifest_before = json.loads(z.read('manifest.json').decode('utf-8'))
            sig_before = manifest_before.get('signature')
            print(f"   Signature before: {sig_before}")
        
        # Now try to sign it manually
        print("\n   Attempting manual signing...")
        try:
            from epi_recorder.signing import sign_epi_file
            
            # Make sure default key exists
            try:
                subprocess.run(['epi', 'keys', 'generate', '--name', 'default'], 
                             capture_output=True, text=True, check=False, timeout=5)
            except:
                pass
            
            # Sign the file
            sign_epi_file(str(test_file_2), 'default')
            
            # Check if it worked
            with zipfile.ZipFile(test_file_2, 'r') as z:
                manifest_after = json.loads(z.read('manifest.json').decode('utf-8'))
                sig_after = manifest_after.get('signature')
                
                if sig_after:
                    print(f"✅ MANUAL SIGNING WORKED: {sig_after[:60]}...")
                    manual_sign_works = True
                else:
                    print("❌ Manual signing failed - still no signature")
                    manual_sign_works = False
                    
        except Exception as e:
            print(f"❌ Manual signing error: {e}")
            import traceback
            traceback.print_exc()
            manual_sign_works = False
    else:
        print("❌ File creation failed")
        manual_sign_works = False
        
except Exception as e:
    print(f"❌ Error during manual test: {e}")
    import traceback
    traceback.print_exc()
    manual_sign_works = False

# Test 5: Verify command
print("\nTEST 5: Testing 'epi verify' command")
print("-"*70)
if test_file_1.exists():
    try:
        result = subprocess.run(['epi', 'verify', str(test_file_1)], 
                              capture_output=True, text=True, timeout=10)
        print("Output from 'epi verify':")
        print(result.stdout)
        
        if result.returncode == 0 and 'HIGH' in result.stdout:
            print("✅ Verification passed!")
            verify_works = True
        else:
            print("❌ Verification failed or suspicious output")
            verify_works = False
    except Exception as e:
        print(f"❌ Verify command error: {e}")
        verify_works = False
else:
    print("⚠️  No file to verify (test 3 failed)")
    verify_works = False

# Cleanup
print("\n" + "="*70)
print("🧹 CLEANUP")
print("="*70)
for f in [test_file_1, test_file_2]:
    if f.exists():
        f.unlink()
        print(f"Deleted: {f}")

# Summary
print("\n" + "="*70)
print("📊 TEST RESULTS SUMMARY")
print("="*70)

results = []
results.append(("auto_sign=True works", auto_sign_works))
results.append(("Manual signing works", manual_sign_works))
results.append(("Verification works", verify_works))

all_passed = all(r[1] for r in results)

for test_name, passed in results:
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"{status}: {test_name}")

print("\n" + "="*70)
if all_passed:
    print("🎉 ALL TESTS PASSED!")
    print("="*70)
    print("\n✅ The notebook signing will work correctly!")
    print("✅ auto_sign=True is working")
    print("✅ Manual backup is available")
    print("✅ Verification works")
    print("\n➡️  CONCLUSION: EPI_DEMO_demo_FINAL.ipynb is READY FOR INVESTORS")
else:
    print("⚠️  SOME TESTS FAILED")
    print("="*70)
    
    if auto_sign_works:
        print("\n✅ Good news: auto_sign=True works!")
        print("   The notebook should work fine.")
    else:
        print("\n⚠️  auto_sign=True doesn't work in this environment")
        
        if manual_sign_works:
            print("✅ But manual signing works!")
            print("   The backup system in the notebook will handle this.")
        else:
            print("❌ Manual signing also failed")
            print("   This needs investigation!")
    
    if not manual_sign_works and not auto_sign_works:
        print("\n🚨 CRITICAL: Neither auto nor manual signing works!")
        print("   Possible causes:")
        print("   1. Keys not properly initialized")
        print("   2. epi-recorder version issue")
        print("   3. Permission problems")
        print("\n   Try running: epi keys generate --name default")

print("\n" + "="*70)
print("Test completed at:", time.strftime("%Y-%m-%d %H:%M:%S"))
print("="*70)

# Exit code
sys.exit(0 if all_passed else 1)
