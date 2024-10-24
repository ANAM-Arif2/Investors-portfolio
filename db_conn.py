from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Load the environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=60 * 5, pool_pre_ping=True, pool_use_lifo=True, pool_timeout=30)
    # Try to connect to the database to verify the connection
    with engine.connect() as connection:
        print("Database connection successful.")

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()
except SQLAlchemyError as e:
    print(f"Database connection failed: {e}")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


