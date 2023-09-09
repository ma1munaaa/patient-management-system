from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///my_healthcare.db"
engine = create_engine(DATABASE_URL)

# Create a Session class for interacting with the database
Session = sessionmaker(bind=engine)
