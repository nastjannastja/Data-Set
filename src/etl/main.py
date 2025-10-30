from .extract import read_data
from .transform import transform_data_types, clean_data, validate_data
from .load import (
    save_data_to_parquet,
    write_data_to_database,
    validate_db_data,
    get_db_connection,
)
from dotenv import load_dotenv
from dataclasses import dataclass
import argparse
import os


@dataclass
class Config:
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int = 5432


def load_environment_variables() -> Config:
    load_dotenv()
    return Config(
        DB_HOST=os.getenv("DB_HOST", "localhost"),
        DB_PORT=int(os.getenv("DB_PORT", "5432")),
        DB_USER=os.getenv("DB_USER", "user"),
        DB_PASSWORD=os.getenv("DB_PASSWORD", "password"),
        DB_NAME=os.getenv("DB_NAME", "database"),
    )


def etl_process(etl_config: Config, table_name: str) -> None:
    df = None

    print("Extracting data...")
    df = read_data()

    print("Transforming data...")
    if df is None:
        print("No data to transform.")
        return
    df = clean_data(df)
    df = transform_data_types(df)
    if not validate_data(df):
        raise ValueError("Data validation failed")

    print("Loading data...")
    if df is None:
        print("No data to load. Did you skip previous steps?")
        return
    save_data_to_parquet(df)
    conn = get_db_connection(table_name)
    write_data_to_database(df, conn)
    if not validate_db_data():
        raise ValueError("Database data validation failed")

    print("ETL process completed successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple CLI for ETL process")
    parser.add_argument("--table_name", type=str, help="Database table name")
    args = parser.parse_args()

    config: Config = load_environment_variables()
    etl_process(config, table_name=args.table_name)
