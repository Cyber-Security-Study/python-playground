from marshmallow import Schema, fields, pprint, post_load


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{} is {} years old'.format(self.name, self.age)


class PersonSchema(Schema):
    name = fields.String()
    age = fields.Integer()

    # Auto load the data into the
    # Person object. Unpack and use the
    # named variables as kwargs
    @post_load
    def create_person(self, data):
        return Person(**data)


input_dict = {}

input_dict['name'] = input('What is your name? ')
input_dict['age'] = input('How old are you? ')

schema = PersonSchema()
result = schema.load(input_dict)

pprint(result.data)