from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
POSTGRES_DB = config("POSTGRES_DB")
POSTGRES_LOCAL_HOST = config("POSTGRES_LOCAL_HOST")
POSTGRES_LOCAL_PORT = config("POSTGRES_LOCAL_PORT")

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_LOCAL_HOST}:{POSTGRES_LOCAL_PORT}/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
try:
    with engine.connect() as connection_str:
        print("Successfully connected to the PostgreSQL database")
except Exception as e:
    print(f"Sorry failed to connect: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Base.metadata.create_all(engine)
