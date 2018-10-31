from data_management.app import db

# models definition
class CountryModel(db.Model):
    __tablename__ = 'country'

    short_name = db.Column(db.String(3), primary_key=True)
    full_name = db.Column(db.String(255))

    def __repr__(self):
        return '<Country {}>'.format(self.full_name)


class Migration(db.Model):
    __tablename__ =  'migrations'
    id = db.Column(db.Integer, primary_key=True)
    dest_country = db.Column(db.String(3), db.ForeignKey('country.short_name'))
    source_country = db.Column(db.String(3), db.ForeignKey('country.short_name'))
    year = db.Column(db.Integer)
    total = db.Column(db.Integer)
