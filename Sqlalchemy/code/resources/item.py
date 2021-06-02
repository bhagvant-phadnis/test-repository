import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This fiels can not be blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message" : "Item not found"}, 404



    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':"An item with name '{}' already exists,".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name,data['price'])
        """
        conn = sqlite3.connect()
        cursor = conn.cusrsor()

        insert_query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(insert_query, (item['name'],item['price']))

        conn.commit()
        conn.close()
        """
        try:
            item.insert()
        except:
            return {"message" : "An error occurred inserting the item"}, 500  #server error
        return item.json(), 201


    # delete item

    def delete(self,name):
#        global items
#        items = list(filter(lambda x: x['name'] != name, items))
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        delete_query = "DELETE FROM items WHERE name = ?"
        cursor.execute(delete_query, (name,))

        conn.commit()
        conn.close()

        return {'message':'Item deleted'}

    def put(self, name):

        data = Item.parser.parse_args()

        """
        item = next(filter(lambda x: x['name'] == name, items), None)

        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
        """
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message" : "An error occurred while inserting an item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message" : "An error occurred while updating an item"}, 500

        return update_item.json()


class ItemList(Resource):
    def get(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        select_query = "SELECT * FROM items"
        result = cursor.execute(select_query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price':row[1]})

#        conn.commit()
        conn.close()
        return {'items':items}
