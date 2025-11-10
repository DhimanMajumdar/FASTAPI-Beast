from sqlmodel import SQLModel,create_engine

#SQLite Database file(Local)
DATABASE_URL="sqlite:///./books.db"

# Engine helps to connect database to SQlmodel
engine=create_engine(DATABASE_URL,echo=True)

# This function will create all the tables 
def init_db():
    SQLModel.metadata.create_all(engine)