


from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from db import get_engine

engine = get_engine()
Base = automap_base()
Base.prepare(engine, reflect=True)

Session = sessionmaker(bind=engine)

def reflect_db():
    return Base, engine

def get_session():
    return Session()

