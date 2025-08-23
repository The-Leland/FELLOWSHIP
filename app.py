


import os
from flask import Flask
from flask_marshmallow import Marshmallow

from db import init_db, db
from util.blueprints import register_blueprints  # Confirm folder name is util, not utils

flask_host = os.environ.get("FLASK_HOST", "127.0.0.1")
flask_port = int(os.environ.get("FLASK_PORT", 5000))

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_scheme}{database_user}@{database_address}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)
ma = Marshmallow(app)

register_blueprints(app)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")

@app.route('/')
def index():
    return {"message": "Welcome to the Fellowship Management API"}

if __name__ == '__main__':
    create_tables()
    app.run(host=flask_host, port=flask_port)
