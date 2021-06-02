import sqlite3
from flask_restful import Resource,reqparse     #reqparse for request parsing
from models.User import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This fiels can not be blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This fiels can not be blank!"
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        # Prevent duplicate user signing

        if UserModel.find_by_username(data['username']):
            return {"message" : "A user with name {} already exists".format(data['username'])},400

        # inser new user

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        insert_query = "INSERT INTO users VALUES (NULL,?,?)"

        cursor.execute(insert_query, (data['username'], data['password']))

        conn.commit()
        conn.close()

        return ('"message" : "User created successfully."'), 201
