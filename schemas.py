from marshmallow import Schema, fields


class PlainPokemonSchema(Schema):
    id = fields.Int(dump_only=True, metadata={"description": "Pokémon ID"})
    name = fields.Str(required=True, metadata={"description": "Pokémon Name"})


class PlainAbilitiesSchema(Schema):
    id = fields.Int(dump_only=True, metadata={"description": "Ability ID"})
    name = fields.Str(required=True, metadata={"description": "Ability Name"})


class PokemonSchema(PlainPokemonSchema):
    abilities = fields.List(
        fields.Nested(PlainAbilitiesSchema()),
        dump_only=True,
        metadata={"description": "Pokémon Abilities"},
    )
