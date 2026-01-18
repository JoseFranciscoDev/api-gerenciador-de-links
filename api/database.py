from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

engine = create_engine(
    "sqlite:///database.db", 
    connect_args={"check_same_thread": False}  
    )

Base = declarative_base()


def get_db():
    with Session(engine) as session:
        yield session
        
