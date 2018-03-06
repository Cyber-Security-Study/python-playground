from marshmallow import Schema, fields, pprint


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{} is {} years old'.format(self.name, self.age)


class PersonSchema(Schema):
    name = fields.String()
    age = fields.Integer()


input_dict = {}

input_dict['name'] = input('What is your name? ')
input_dict['age'] = input('How old are you? ')

person = Person(name=input_dict['name'], age=input_dict['age'])

schema = PersonSchema()
result = schema.dump(person)
pprint(result.data)