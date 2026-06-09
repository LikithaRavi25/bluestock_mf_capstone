"""
Master Pipeline Runner
Bluestock MF Analytics Platform
"""

import subprocess


scripts = [
    "scripts/load_sqlite.py",
    "scripts/verify_counts.py",
    "scripts/amfi_validation.py",
    "scripts/explore_fund_master.py",
    "scripts/live_nav_fetch.py",
    "scripts/multi_nav_fetch.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(["python", script])

print("Pipeline completed successfully.")