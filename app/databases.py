from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import create_engine
from .Util.Config import Database_url

engine = create_engine(Database_url)

Sessionlocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
