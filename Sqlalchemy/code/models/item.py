from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # To fetch the details
        return cls.query.filter_by(name=name).first()           # SELECT * from items where name=name  LIMIT 1
#        return cls.query.filter_by(name=name, id=1)             # SELECT * from items where name=name and id=1
    def save_to_db(self):
        # To insert the details using SQLAlchemy
        db.session.add(self)                                       # add() this method perform insert as well as update operation.
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
