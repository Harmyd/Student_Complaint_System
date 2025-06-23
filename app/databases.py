from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import create_engine

Database_url="postgresql://hamid:ST1ikXcVptWgVaZtIpjnFemAxk0g4BEb@dpg-d1csrremcj7s73bav350-a.oregon-postgres.render.com/student_complaint"
engine = create_engine(Database_url)

Sessionlocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
