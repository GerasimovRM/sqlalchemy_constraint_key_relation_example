from pathlib import Path
import os
from dotenv import load_dotenv

if not os.getenv("DOCKER"):
    load_dotenv(Path(__file__).parent.joinpath('.env').resolve())

SQL_ECHO = os.getenv("SQL_ECHO") in ("True", "true", "1")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_BASE_URL = f"{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
DATABASE_URL = f"postgresql+asyncpg://{DATABASE_BASE_URL}"
DATABASE_URL_SYNC = f"postgresql+psycopg2://{DATABASE_BASE_URL}"
