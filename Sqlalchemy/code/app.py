#Adding authentication

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
#from flask.helpers import _endpoint_from_view_func

from security import authenticate,identity
from resources.User import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'     # TO know sqlalchemy, where to find db,    currenlty it is root directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key='Mahesh'
api = Api(app)

jwt = JWT(app, authenticate, identity)   #/auth

"""
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This fiels can not be blank!"
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
#        for item in items:
#            if item['name'] == name:
#                return item
#        return {'item' : None}, 404
        return {'Item' : item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message':"An item with name '{}' already exists,".format(name)}, 400
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    # delete item

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message':'Item deleted'}

    def put(self, name):

        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
class ItemList(Resource):
    def get(self):
        return {'items':item}

"""

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
