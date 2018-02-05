from app import db

class Product(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64), index=True, unique=True)
    category=db.Column(db.String(64), index=True)
    characteristics = db.relationship('Characteristic', backref='id_prod', lazy='dynamic')



class Characteristic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    price = db.Column(db.Integer, index=True)

    proc = db.Column(db.String(140))
    chastot= db.Column(db.String(30))
    oper_m= db.Column(db.String(30))
    hdd= db.Column(db.String(30))
    monit= db.Column(db.String(30))
    video= db.Column(db.String(30))
    weight= db.Column(db.String(30))
    optic= db.Column(db.String(30))
    g4= db.Column(db.String(30))
    blue= db.Column(db.String(30))
    wifi= db.Column(db.String(30))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


