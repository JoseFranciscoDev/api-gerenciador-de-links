from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine(
    "sqlite:///database.db", 
    connect_args={"check_same_thread": False}  
    )

class Base(DeclarativeBase):
    pass



def get_db():
    with Session(engine) as session:
        yield session
        

