import pandas as pd
import os


def read_data() -> pd.DataFrame:
    file_id = "1qkzC64D8GnLRwpQFl6vhD1C7tLgM6LM6"
    file_url = f"https://drive.google.com/uc?id={file_id}"
    df = pd.read_csv(file_url)

    os.makedirs("data/raw", exist_ok=True)
    raw_path = "data/raw/raw_data.csv"
    df.to_csv(raw_path, index=False)
    print(f"данные сохранены в {raw_path}")

    return df
