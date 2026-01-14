"""
EMERGENCY RESTORE - Revert notebook to backup
"""

import shutil
from pathlib import Path

backup_path = Path(r"c:\Users\dell\OneDrive\Desktop\EPI_DEMO_demo.ipynb.backup")
notebook_path = Path(r"c:\Users\dell\OneDrive\Desktop\EPI_DEMO_demo.ipynb")

print("=" * 70)
print("EMERGENCY RESTORE")
print("=" * 70)

if not backup_path.exists():
    print(f"\nERROR: Backup file not found at: {backup_path}")
else:
    print(f"\nBackup found: {backup_path}")
    print(f"Restoring to: {notebook_path}")
    
    # Copy backup to original
    shutil.copy2(backup_path, notebook_path)
    
    print("\n" + "=" * 70)
    print("RESTORED SUCCESSFULLY!")
    print("=" * 70)
    print("\nYour original notebook has been restored from backup.")
    print("The broken changes have been reverted.")
    print("\nYou can now:")
    print("  1. Upload the restored notebook to Google Colab")
    print("  2. OR tell me what was wrong and I'll fix it differently")

print("\n" + "=" * 70)
