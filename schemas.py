from marshmallow import Schema, fields


class PlainPokemonSchema(Schema):
    id = fields.Int(dump_only=True, description="Pokémon ID")
    name = fields.Str(required=True, description="Pokémon Name")


class PlainAbilitiesSchema(Schema):
    id = fields.Int(dump_only=True, description="Ability Id")
    name = fields.Str(required=True, description="Ability Name")


class PokemonSchema(PlainPokemonSchema):
    abilities = fields.List(
        fields.Nested(PlainAbilitiesSchema()),
        dump_only=True,
        description="Pokémon's abilities",
    )
