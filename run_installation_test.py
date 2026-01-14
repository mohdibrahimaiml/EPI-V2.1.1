#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EPI Recorder - Multiple Installation Test
Tests the reliability of EPI Recorder installation by installing it multiple times.
"""

import subprocess
import time
import random
import sys
from datetime import datetime

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except:
        pass

def install_epi():
    """Install epi-recorder and return success status"""
    try:
        result = subprocess.run(
            ['pip', 'install', '-q', 'epi-recorder'],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0, result.stderr
    except Exception as e:
        return False, str(e)

def uninstall_epi():
    """Uninstall epi-recorder"""
    try:
        subprocess.run(
            ['pip', 'uninstall', '-y', '-q', 'epi-recorder'],
            capture_output=True,
            timeout=30
        )
        return True
    except:
        return False

def verify_epi():
    """Verify epi-recorder is installed and working"""
    try:
        # Check if epi command is available
        result = subprocess.run(
            ['epi', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return True, result.stdout.strip()
        
        # Fallback: try python -m method
        result = subprocess.run(
            ['python', '-m', 'epi_recorder', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout.strip()
    except Exception as e:
        return False, str(e)

def display_progress(iteration, total, status, results):
    """Display progress with fancy formatting"""
    progress = (iteration / total) * 100
    bar_length = 40
    filled = int(bar_length * iteration / total)
    bar = '#' * filled + '-' * (bar_length - filled)
    
    print(f"\n{'='*60}")
    print(f"[>] EPI Recorder Installation Test")
    print(f"{'='*60}")
    print(f"Progress: [{bar}] {progress:.1f}%")
    print(f"Iteration: {iteration}/{total}")
    print(f"Status: {status}")
    print(f"{'='*60}")
    print(f"\n[STATS] Current Statistics:")
    print(f"  [+] Successful Installs: {results['successful_installs']}")
    print(f"  [-] Failed Installs: {results['failed_installs']}")
    print(f"  [+] Successful Verifications: {results['successful_verifications']}")
    print(f"  [-] Failed Verifications: {results['failed_verifications']}")
    if results['install_times']:
        avg_time = sum(results['install_times']) / len(results['install_times'])
        print(f"  [T] Average Install Time: {avg_time:.2f}s")
    print(f"{'='*60}\n")

def main():
    # Set random number of installations (1-50)
    NUM_INSTALLATIONS = random.randint(1, 50)
    
    print(f"\n{'='*60}")
    print("[!] EPI RECORDER INSTALLATION STRESS TEST")
    print(f"{'='*60}")
    print(f"[*] Randomly selected: {NUM_INSTALLATIONS} installations")
    print(f"[*] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Statistics tracking
    results = {
        'successful_installs': 0,
        'failed_installs': 0,
        'successful_verifications': 0,
        'failed_verifications': 0,
        'install_times': [],
        'errors': []
    }
    
    # Main installation loop
    for i in range(1, NUM_INSTALLATIONS + 1):
        # Display progress
        print(f"\n[>] Starting installation #{i}...")
        
        # Install
        start_time = time.time()
        install_success, install_error = install_epi()
        install_time = time.time() - start_time
        
        if install_success:
            results['successful_installs'] += 1
            results['install_times'].append(install_time)
            print(f"[+] Installation #{i} successful ({install_time:.2f}s)")
            
            # Verify installation
            print(f"[>] Verifying installation #{i}...")
            verify_success, verify_output = verify_epi()
            
            if verify_success:
                results['successful_verifications'] += 1
                print(f"[+] Verification successful: {verify_output}")
            else:
                results['failed_verifications'] += 1
                results['errors'].append(f"Iteration {i}: Verification failed - {verify_output}")
                print(f"[-] Verification failed: {verify_output}")
        else:
            results['failed_installs'] += 1
            results['errors'].append(f"Iteration {i}: Install failed - {install_error}")
            print(f"[-] Installation #{i} failed: {install_error}")
        
        # Show current stats
        display_progress(i, NUM_INSTALLATIONS, f"Completed iteration {i}", results)
        
        # Uninstall before next iteration (except last one)
        if i < NUM_INSTALLATIONS:
            print(f"[>] Uninstalling before next iteration...")
            uninstall_epi()
            time.sleep(0.5)  # Brief pause between cycles
    
    # Final Results
    total_attempts = NUM_INSTALLATIONS
    install_success_rate = (results['successful_installs'] / total_attempts) * 100
    verify_success_rate = (results['successful_verifications'] / max(results['successful_installs'], 1)) * 100
    avg_install_time = sum(results['install_times']) / len(results['install_times']) if results['install_times'] else 0
    min_install_time = min(results['install_times']) if results['install_times'] else 0
    max_install_time = max(results['install_times']) if results['install_times'] else 0
    
    print("\n" + "="*60)
    print("[!] FINAL RESULTS")
    print("="*60)
    print(f"\n[STATS] Installation Statistics:")
    print(f"  Total Attempts: {total_attempts}")
    print(f"  [+] Successful: {results['successful_installs']}")
    print(f"  [-] Failed: {results['failed_installs']}")
    print(f"  [%] Success Rate: {install_success_rate:.1f}%")
    
    print(f"\n[STATS] Verification Statistics:")
    print(f"  [+] Successful: {results['successful_verifications']}")
    print(f"  [-] Failed: {results['failed_verifications']}")
    print(f"  [%] Success Rate: {verify_success_rate:.1f}%")
    
    print(f"\n[TIME] Timing Statistics:")
    print(f"  Average: {avg_install_time:.2f}s")
    print(f"  Fastest: {min_install_time:.2f}s")
    print(f"  Slowest: {max_install_time:.2f}s")
    
    # Display errors if any
    if results['errors']:
        print(f"\n[!] Errors Encountered ({len(results['errors'])}):\n")
        for error in results['errors'][:5]:  # Show first 5 errors
            print(f"  * {error}")
        if len(results['errors']) > 5:
            print(f"  ... and {len(results['errors']) - 5} more")
    else:
        print(f"\n[+] No errors encountered!")
    
    # Final verdict
    print(f"\n" + "="*60)
    if install_success_rate == 100 and verify_success_rate == 100:
        print("[!!!] VERDICT: PERFECT! All installations successful!")
    elif install_success_rate >= 95:
        print("[+] VERDICT: EXCELLENT! Installation is highly reliable.")
    elif install_success_rate >= 80:
        print("[+] VERDICT: GOOD! Installation is mostly reliable.")
    else:
        print("[-] VERDICT: NEEDS ATTENTION! Installation has issues.")
    print("="*60)
    
    print(f"\n[*] Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "="*60)
    
    # Final verification
    print("\n[>] Verifying final installation...\n")
    subprocess.run(['epi', '--version'])

if __name__ == "__main__":
    main()
