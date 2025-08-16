import pandas as pd
from pathlib import Path

# Create DataFrame
df = pd.DataFrame([
    {"Name": "ABC", "Age": 10, "City": "NY"},
    {"Name": "XYZ", "Age": 20, "City": "LA"},
    {"Name": "PQR", "Age": 10, "City": "MX"} ,
    {"Name" : "ASD" , "Age" : 10 , "City" :"AB"}
])

# Define directory and file path using pathlib
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "sample_data.csv"

# Save to CSV
df.to_csv(file_path, index=False)

print(f"CSV file saved at: {file_path.resolve()}")
