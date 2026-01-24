# Welcome to EPI!

import time

print("="*40)
print("   Hello from your first EPI recording!")
print("="*40)

print("\n1. Doing some math...")
result = 123 * 456
print(f"   123 * 456 = {result}")

print("\n2. Creating a file...")
with open("epi_hello.txt", "w") as f:
    f.write(f"Calculation result: {result}")
print("   Saved 'epi_hello.txt'")

print("\n3. Finishing up...")
time.sleep(0.5)
print("[OK] Done! Now check the browser!")
