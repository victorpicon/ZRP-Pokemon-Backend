from db import db


class AbilityModel(db.Model):
    __tablename__ = "abilities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)
