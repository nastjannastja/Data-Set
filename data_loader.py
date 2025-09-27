import pandas as pd

file_id = "1qkzC64D8GnLRwpQFl6vhD1C7tLgM6LM6"
file_url = f"https://drive.google.com/uc?id={file_id}"

raw_data = pd.read_csv(file_url)

first = raw_data.head(10)
print(first)
