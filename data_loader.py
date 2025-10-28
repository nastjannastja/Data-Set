import pandas as pd
import pyarrow.parquet as pq

file_id = "1qkzC64D8GnLRwpQFl6vhD1C7tLgM6LM6"
file_url = f"https://drive.google.com/uc?id={file_id}"

raw_data = pd.read_csv(file_url)

raw_data = raw_data.astype(
    {
        "id": "Int32",
        "Gender": "string",
        "Age": "Int32",
        "City": "string",
        "Profession": "string",
        "Academic Pressure": "Int32",
        "Work Pressure": "Int32",
        "CGPA": "float32",
        "Study Satisfaction": "Int32",
        "Job Satisfaction": "Int32",
        "Sleep Duration": "string",
        "Dietary Habits": "string",
        "Degree": "string",
        "Have you ever had suicidal thoughts ?": "string",
        "Work/Study Hours": "Int32",
        "Financial Stress": "string",
        "Family History of Mental Illness": "string",
        "Depression": "int8",
    }
)
print(raw_data.dtypes)
raw_data.to_parquet("dataset.parquet", engine="pyarrow", index=False)

