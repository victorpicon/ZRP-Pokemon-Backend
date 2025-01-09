from marshmallow import Schema, fields


class PlainPokemonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainAbilitiesSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PokemonSchema(PlainPokemonSchema):
    abilities = fields.List(fields.Nested(PlainAbilitiesSchema()), dump_only=True)
