from marshmallow import Schema, fields, pprint, post_load, ValidationError


class Person(object):
    def __init__(self, name, age, email, location):
        self.name = name
        self.age = age
        self.email = email
        self.location = location

    def __repr__(self):
        return '{} is {} years old, email is {}, location is {}'.format(self.name, self.age, self.email, self.location)


def validate_age(age):
    if age < 25:
        raise ValidationError('You are too young!')


class PersonSchema(Schema):
    name = fields.String()
    age = fields.Integer(validate=validate_age)
    email = fields.Email()
    location = fields.String(required=True)

    # Auto load the data into the
    # Person object. Unpack and use the
    # named variables as kwargs
    @post_load
    def create_person(self, data):
        return Person(**data)


input_dict = {}

input_dict['name'] = input('What is your name? ')
input_dict['age'] = input('How old are you? ')
input_dict['email'] = input('What\'s your email? ')
input_dict['location'] = input('What\'s your location? ')

schema = PersonSchema()
result = schema.load(input_dict)

pprint(result)