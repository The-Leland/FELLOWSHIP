


import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/middleearth")

def get_engine():
    return create_engine(DATABASE_URL, echo=True)
