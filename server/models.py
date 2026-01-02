from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bakery(db.Model):
    __tablename__ = 'bakeries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    baked_goods = db.relationship('BakedGood', backref='bakery')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class BakedGood(db.Model):
    __tablename__ = 'baked_goods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'bakery_id': self.bakery_id
        }