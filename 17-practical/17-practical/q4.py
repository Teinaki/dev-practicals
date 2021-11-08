# For the SerialiseMe class below:
# Part 1: Write a custom JSON Encoder that can be used with json.dumps()
# to serialise objects of this type to JSON.
#
# Part 2: Write a marshmallow schema and use it to serialise and
# deserialise objects of this type. Note that these produce and
# read dictionaries, not JSON strings (but the dictionaries are easily
# converted to/from JSON).

import json

z = 1 + 2j
# z is a complex number - a type supported natively in Python but not JSON.

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        return json.JSONEncoder.default(self, obj)

json_z = json.dumps(z, cls=ComplexEncoder)

class SerialiseMe:
    def __init__(self, my_str, my_int, my_bool):
        self.my_str = my_str
        self.my_int = my_int
        self.my_bool = my_bool

    def dumps(self):
        return json.dumps({'my_str': self.my_str, 'my_int': self.my_int, 'my_bool': self.my_bool})

    @classmethod
    def loads(cls, js):
        data = json.loads(js)
        return cls(data['my_str'], data['my_int'], data['my_bool'])

sample = SerialiseMe('spam', 42, False)
json_serialise = sample.dumps()   
restored_serialise = sample.loads(json_serialise)

from marshmallow import Schema, fields # you will need to pip install marshmallow

class SerialiseMe:
    def __init__(self, my_str, my_int, my_bool):
        self.my_str = my_str
        self.my_int = my_int
        self.my_bool = my_bool

class SerialiseSchema(Schema):
    my_str = fields.Str(required=True)
    my_int = fields.Integer()
    my_bool = fields.Bool()

    @post_load
    def make_serialised(self, data, **kwargs):
        return SerialiseMe(**data)


sample = SerialiseMe('spam', 42, False)        
serialise_schema = SerialiseSchema()
serialised = serialise_schema.dump(sample)  # returns a dict, not json
deserialised = serialise_schema.load(serialised)