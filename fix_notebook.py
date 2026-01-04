import json

# Load the notebook
with open('Fibonacci_Hashing_Demo.ipynb', 'r') as f:
    nb = json.load(f)

# Find and fix the imports cell
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'import subprocess' in source:
            # This is the imports cell - remove unused imports
            new_source = """import json
import time
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

# Fibonacci hashing constant
FIB_HASH_64_MAGIC = 11400714819323198485

print("✓ Imports successful")
print(f"✓ Fibonacci magic constant: {FIB_HASH_64_MAGIC}")"""
            cell['source'] = [new_source]
            print("✓ Removed unused imports: subprocess, os, tempfile")
            break

# Save the updated notebook
with open('Fibonacci_Hashing_Demo.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

print("✓ Notebook updated successfully")
