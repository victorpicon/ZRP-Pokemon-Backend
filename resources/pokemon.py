from db import db
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.ability import AbilityModel
from models.pokemon import PokemonModel
from schemas import PokemonSchema
import requests

blp = Blueprint("pokemons", __name__, description="Operations on pokemons")


@blp.route("/pokemon")
class PokemonList(MethodView):
    @blp.response(200, PokemonSchema(many=True))
    def get(self):
        pokemons = PokemonModel.query.all()
        if not pokemons:
            abort(404, message="No pokemons found")
        return pokemons


@blp.route("/pokemon/<string:name>")
class Pokemon(MethodView):
    def get(self, name):
        pokemon = PokemonModel.query.filter_by(name=name.lower()).first()
        if pokemon:
            abilities = [ability.name for ability in pokemon.abilities]
        else:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
            if response.status_code != 200:
                abort(404, message=f"Pokémon '{name}' not found in PokéAPI.")

            data = response.json()
            abilities = sorted(
                ability["ability"]["name"] for ability in data["abilities"]
            )

            pokemon = PokemonModel(name=name.lower())
            db.session.add(pokemon)
            for ability_name in abilities:
                db.session.add(AbilityModel(name=ability_name, pokemon=pokemon))
            db.session.commit

        return {"name": pokemon.name, "abilities": abilities}
