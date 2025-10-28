import pandas as pd
import pyarrow.parquet as pq

file_id = "1qkzC64D8GnLRwpQFl6vhD1C7tLgM6LM6"
file_url = f"https://drive.google.com/uc?id={file_id}"

raw_data = pd.read_csv(file_url)

raw_data.rename(
    columns={"Have you ever had suicidal thoughts ?": "Suicidal_Thoughts"}, inplace=True
)

raw_data.columns = (
    raw_data.columns.str.strip()
    .str.replace(" ", "_", regex=False)
    .str.replace("/", "_or_", regex=False)
)

raw_data = raw_data.astype(
    {
        "id": "Int32",
        "Gender": "string",
        "Age": "Int32",
        "City": "string",
        "Profession": "string",
        "Academic_Pressure": "Int32",
        "Work_Pressure": "Int32",
        "CGPA": "float32",
        "Study_Satisfaction": "Int32",
        "Job_Satisfaction": "Int32",
        "Sleep_Duration": "string",
        "Dietary_Habits": "string",
        "Degree": "string",
        "Suicidal_Thoughts": "bool",
        "Work_or_Study_Hours": "Int32",
        "Financial_Stress": "string",
        "Family_History_of_Mental_Illness": "bool",
        "Depression": "int8",
    }
)
print(raw_data.dtypes)
raw_data.to_parquet("dataset.parquet", engine="pyarrow", index=False)
