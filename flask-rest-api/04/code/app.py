from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # The client should really check if name exists before
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'An item with name {} already exists.'.format(name)}, 400

        # This section only returns if above is `False`:
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201  # 'Created' browser code

    def delete(self, name):
        # return a new list without the one we're deleting:
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    # PUT output should never change:
    # i.e: it should only create, or modify
    #      multiple objects should not be created
    def put(self, name):
        # Only allow certain elements to be modified.
        # - DEPRECATED soon: http://bit.ly/2o63bXb
        # - If any fields other than the ones
        #   declared are passed, they will be ignored (erased)
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )

        data = parser.parse_args()
        print(data['another'])
        item = next(filter(lambda x: x['name'] == name, items), None)

        # Create the item if it doesn't exist ...
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        # Or, update the item if it does
        else:
            item.update(data)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}, 200


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True)