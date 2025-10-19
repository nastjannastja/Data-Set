from sqlalchemy import create_engine

import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_url = os.getenv("DB_URL")
db_port = os.getenv("DB_PORT")
db_root_base = os.getenv("DB_ROOT_BASE")

assert db_url

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}",
    pool_recycle=3600,
)

data = pd.read_parquet("Data-Set/dataset.parquet")

new_column_names = {col: col.lower() for col in data.columns}

data.rename(columns=new_column_names, inplace=True)

data_to_add = data.head(90)


with engine.begin() as conn:
    data_to_add.to_sql(
        name="magomedova",
        con=conn,
        schema="public",
        if_exists="replace",
        index=False,
    )

    result = pd.read_sql(
        "SELECT * FROM public.magomedova LIMIT 6",  # проверка корректности добавления данных
        con=conn,
    )
    print(result)
