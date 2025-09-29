import requests
import xml.etree.ElementTree as ET
import pandas as pd


def load_currencies() -> pd.DataFrame:
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    records = []
    for currency in root.findall("Valute"):
        char_code = currency.find("CharCode").text
        nominal = int(currency.find("Nominal").text)
        name = currency.find("Name").text
        value = float(currency.find("Value").text.replace(",", "."))

        records.append(
            {
                "Тикер": char_code,
                "Номинал": nominal,
                "Название валюты": name,
                "Курс": value,
                "Курс за единицу": value / nominal,
            }
        )

    df = pd.DataFrame(records)
    return df.sort_values(by="Название валюты", ascending=True)


# Пример использования:
if __name__ == "__main__":
    currency_list = load_currencies()
    print(currency_list.head(10).to_string(index=False))
