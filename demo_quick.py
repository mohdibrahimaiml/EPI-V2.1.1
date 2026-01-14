"""
EPI Demo Script - Quick Version (30 seconds)
Perfect for fast demonstrations
"""
import time

print("\n" + "="*60)
print("  EPI QUICK DEMO - 30 Second Workflow")
print("="*60 + "\n")

# Step 1
print("📍 STEP 1: Starting process...")
time.sleep(1)

# Step 2
print("📍 STEP 2: Processing data...")
for i in range(1, 4):
    print(f"   • Item {i} processed ✓")
    time.sleep(0.5)

# Step 3
print("📍 STEP 3: Creating output file...")
with open("quick_demo_output.txt", "w") as f:
    f.write("EPI Quick Demo - Success!\n")
    f.write("All operations recorded and signed.\n")
print("   ✓ File saved: quick_demo_output.txt")
time.sleep(0.5)

# Complete
print("\n" + "="*60)
print("✅ DEMO COMPLETE!")
print("="*60)
print("\n🔐 EPI captured everything in a tamper-proof package!")
print("👀 View the timeline in your browser now.\n")
