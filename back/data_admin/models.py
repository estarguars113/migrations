from data_admin.app import db

# models definition
class CountryModel(db.Model):
    __tablename__ = 'country'

    short_name = db.Column(db.String(5), primary_key=True)
    full_name = db.Column(db.String(255))

    def __init__(self, short_name, full_name):
        self.short_name = short_name
        self.full_name = full_name

    def __repr__(self):
        return '<Country {}>'.format(self.full_name)


class Migration(db.Model):
    __tablename__ =  'migrations'

    id = db.Column(db.Integer, primary_key=True)
    dest_country = db.Column(db.String(5), db.ForeignKey('country.short_name'))
    source_country = db.Column(db.String(5), db.ForeignKey('country.short_name'))
    year = db.Column(db.Integer)
    total = db.Column(db.Integer)
    gender= db.Column(db.String(15))
    age_range  = db.Column(db.String(15))

