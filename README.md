# Data-Set
## 1. **Общая информация о датасете** 
 Данный датасет представляет собой результаты опроса студентов по уровню депрессии, собранные в рамках исследования факторов психического здоровья студентов в виде таблицы по нескольким признакам.
 
**Ссылка на датасет:** https://drive.google.com/drive/folders/10_vT1Pt0w413sym9fv7I4KWLi_7YApd0?dmr=1&ec=wgc-drive-globalnav-goto

**Исходные данные с kaggle.com:** https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset?resource=download

## 2. Загрузка poetry
Для того, чтобы установить все необходимые зависимости, нужно:

• Находиться в одной папке с файлом pyproject.toml

• Иметь установленный python(в виртуальном окружении или в целом, не важно)

• Иметь установленный poetry (pip install poetry)

• Написать poetry install --no-root

После этого будет произведена установка всех необходимых библиотек для работы с кодом проекта.

<img width="1850" height="278" alt="{A147C982-0714-4980-BAC2-2E998C418620}" src="https://github.com/user-attachments/assets/edc2678a-a906-4d82-b979-312356896179" />

С помощью команды dtypes, можно удостовериться, что все типы данных скастовались корректно
<img width="1313" height="466" alt="{E3BDA512-798D-4E3F-A169-AE23EB2F16C2}" src="https://github.com/user-attachments/assets/86f6652a-7346-442d-a96d-ee83b3b9997a" />

## 3. Nbviewer 
Ссылка на nbviewer для просмотра рендера ноутбука EDA.ipynb: https://nbviewer.org/github/nastjannastja/Data-Set/blob/main/notebooks/EDA.ipynb?flush=1

## 4. ETL

Репозиторий содержит простой ETL (Extract → Transform → Load), реализованный как пакет etl в src/etl/.

### **Структура ETL**

```
Data-Set/
├─ src/
  ├─ etl/
    ├─ __init__.py
    ├─ extract.py
    ├─ transform.py
    ├─ load.py
    └─ main.py
```

Для корректной работы ETL-процесса пользователю нужно установить несколько библиотек Python, которые обеспечивают работу с обработкой данных (pandas, pyarrow), базой данных (sqlalchemy, psycopg2), переменными окружения (python-dotenv), и типами данных (dataclasses, если Python < 3.7).

```
pip install pandas pyarrow sqlalchemy psycopg2-binary python-dotenv
```

### **extract.py** 

Скачивает CSV с Google Drive по file_id, сохраняет сырые данные в data/raw/raw_data.csv и возвращает DataFrame.

### **transform.py** 

1. Функция clean_data(df)

Переименовывает специфичный столбец "Have you ever had suicidal thoughts ?" на "Suicidal_Thoughts".

Очищает названия колонок: убирает пробелы по краям, заменяет пробелы на _, / на _or_.

Удаляет полностью пустые строки.

2. transform_data_types(df)

Приводит набор колонок к ожидаемым типам (например Int32, string, float32, bool и т.д.).

Возвращает преобразованный DataFrame.

3. validate_data(df)

Проверяет, что df не None, не пустой и у поля id есть ненулевые значения.

Печатает результат валидации и возвращает True/False.

### **load.py** 

1. DBConnection это dataclass с полями соединения и table_name.

2. get_db_connection(table_name) читает переменные окружения и возвращает DBConnection.

3. save_data_to_parquet(df) сохраняет в data/processed/processed_data.parquet.

4. write_data_to_database(df, conn) создаёт движок SQLAlchemy и записывает data_to_add (первые 90 строк df) в таблицу public.<table_name> с if_exists="replace".

### **main.py** 

Вызывает extract.py → transform.py → load.py. CLI принимает --table_name и передаёт его в get_db_connection.

Файл .env должен содержать настройки БД.

### **Запуск**

Запуск через командную строку выглядит следующим образом:
```
python -m src.etl.main --table_name name
```
(Вместо name ваша фамилия)