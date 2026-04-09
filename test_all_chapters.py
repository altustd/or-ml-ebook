#
# Test runner for Chapters 01-05
# Runs each notebook and reports success/failure
#

import subprocess
import sys
from pathlib import Path

notebooks = [
    "notebooks/01-introduction.ipynb",
    "notebooks/02-linear-programming.ipynb",
    "notebooks/03-network-optimization.ipynb",
    "notebooks/04-integer-programming.ipynb",
    "notebooks/05-nonlinear-optimization.ipynb"
]

print("Starting test of Chapters 01–05...\n")
print("=" * 60)

for nb_path in notebooks:
    path = Path(nb_path)
    if not path.exists():
        print(f"❌ {path.name} - File not found")
        continue
    
    print(f"Testing {path.name} ...", end=" ")
    
    try:
        result = subprocess.run([
            "jupyter", "nbconvert", 
            "--to", "notebook", 
            "--execute", 
            "--inplace", 
            "--ExecutePreprocessor.timeout=30",
            str(path)
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Success")
        else:
            print("❌ Failed")
            print("   Error:", result.stderr.strip()[:200])
            
    except subprocess.TimeoutExpired:
        print("❌ Timeout")
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n" + "=" * 60)
print("Testing complete.")
