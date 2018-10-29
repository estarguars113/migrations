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

# models definition
class CountryModel(db.Model):
    __tablename__ = 'country'

    id = db.Column(db.Integer, primary_key=True) # country code
    short_name = db.Column(db.String(3))
    full_name = db.Column(db.String(255))

    def __repr__(self):
        return '<Country {}>'.format(self.full_name)


class Migration(db.Model):
    __tablename__ =  'migrations'
    id = db.Column(db.Integer, primary_key=True)
    dest_country = db.Column(db.Integer, db.ForeignKey('country.id'))
    source_country = db.Column(db.Integer, db.ForeignKey('country.id'))
    year = db.Column(db.Integer)
    total = db.Column(db.Integer)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()