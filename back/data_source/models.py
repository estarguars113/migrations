from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from app import db


class CountryModel(Base):
    __tablename__ = 'country'

    short_name = db.Column(db.String(255), primary_key=True)
    full_name = db.Column(db.String(255))

    def __repr__(self):
        return '<Country {}>'.format(self.short_name)


class Migration(Base):
    __tablename__ =  'migrations'
    id = db.Column(db.Integer, primary_key=True)
    source_country = db.Column(db.Integer, db.ForeignKey('country.id'))
    dest_country = db.Column(db.Integer, db.ForeignKey('country.id'))
    year = db.Column(db.Integer)
    total = db.Column(db.Integer)
