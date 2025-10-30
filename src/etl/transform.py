import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    if "Have you ever had suicidal thoughts ?" in df.columns:
        df = df.rename(
            columns={"Have you ever had suicidal thoughts ?": "Suicidal_Thoughts"}
        )

    df.columns = (
        df.columns.str.strip()
        .str.replace(" ", "_", regex=False)
        .str.replace("/", "_or_", regex=False)
    )

    df = df.dropna(how="all")
    return df


def transform_data_types(df: pd.DataFrame) -> pd.DataFrame:
    df = df.astype(
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
            "Depression": "Int8",
        }
    )

    return df


def validate_data(df: pd.DataFrame) -> bool:
    if df is None:
        print("DataFrame is None")
        return False

    if len(df) == 0:
        print("DataFrame is empty")
        return False

    if "id" in df.columns:
        non_null_ids = df["id"].notna().sum()
        if non_null_ids == 0:
            print("валидация не пройдена")
            return False

    print(f"Validation passed: {len(df)} rows, {df.shape[1]} columns")
    return True
