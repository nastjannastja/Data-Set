import pandas as pd

file_id = "1C7Vb-MzdDAF7R3LeVjhfJRheGExRyzlE"
file_url = f"https://drive.google.com/uc?id={file_id}"

raw_data = pd.read_csv(file_url)     

first = raw_data.head(10)         # выводим на экран первые 10 строк для проверки
print(first)


