


from flask import Flask
from utils.blueprints import register_blueprints

app = Flask(__name__)
register_blueprints(app)

@app.route('/')
def index():
    return {"message": "Welcome to the Fellowship Management API"}

if __name__ == '__main__':
    app.run(debug=True)

