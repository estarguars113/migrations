from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://paolagc:passwd_1@localhost/migrations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from data_admin import models

@app.route('/')
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run()