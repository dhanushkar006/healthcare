# load_test.py
from pathlib import Path
import os
import pandas as pd

p = Path(r"C:\Temp\healthcare_dataset.csv")
print("Path:", p)
print("Exists:", p.exists())
print("Readable (os.access):", os.access(p, os.R_OK))
if p.exists():
    df = pd.read_csv(p)
    print("Loaded rows,cols:", df.shape)
    print(df.head(3).to_string())
else:
    print("File not found at", p)
