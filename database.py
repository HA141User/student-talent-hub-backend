from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PERHATIAN: Ganti 'password_kamu' dengan password PostgreSQL di laptopmu!
# Jika usernamenya bukan 'postgres', ganti juga ya.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/student_talent_hub"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()