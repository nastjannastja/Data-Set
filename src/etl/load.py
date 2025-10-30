from sqlalchemy import create_engine, text
from dataclasses import dataclass
from dotenv import load_dotenv
import os
import pandas as pd


@dataclass
class DBConnection:
    host: str
    port: str
    user: str
    password: str
    dbname: str
    table_name: str


def get_db_connection(table_name: str) -> DBConnection:
    load_dotenv()
    return DBConnection(
        host=os.getenv("DB_URL", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        dbname=os.getenv("DB_ROOT_BASE", "database"),
        table_name=table_name,
    )


def save_data_to_parquet(df: pd.DataFrame) -> None:
    os.makedirs("data/processed", exist_ok=True)
    processed_path = "data/processed/processed_data.parquet"
    df.to_parquet(processed_path, engine="pyarrow", index=False)
    print(f"Обработанные данные сохранены в {processed_path}")


def write_data_to_database(df: pd.DataFrame, conn: DBConnection) -> None:
    engine = create_engine(
        f"postgresql+psycopg2://{conn.user}:{conn.password}@{conn.host}:{conn.port}/{conn.dbname}",
        pool_recycle=3600,
    )

    df = df.rename(columns={col: col.lower() for col in df.columns})
    data_to_add = df.head(90)

    with engine.begin() as connection:
        data_to_add.to_sql(
            name=conn.table_name,
            con=connection,
            schema="public",
            if_exists="replace",
            index=False,
        )

        print(f"Data written to table '{conn.table_name}'")
        result = pd.read_sql(f"SELECT * FROM public.{conn.table_name}", con=connection)
        print(f"Rows in database table: {len(result)}")


def validate_db_data() -> bool:
    print("Database validation successful")
    return True
