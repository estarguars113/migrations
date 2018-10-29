from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.debug = True

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://paolagc:passwd_1@localhost/migrations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()