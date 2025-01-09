from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.pokemon import PokemonModel
from schemas import PokemonSchema

blp = Blueprint("pokemons", __name__, description="Operations on pokemons")


@blp.route("/pokemon")
class Pokemon(MethodView):
    @blp.response(200, PokemonSchema(many=True))
    def get(self):
        pokemons = PokemonModel.query.all()
        if not pokemons:
            abort(404, message="No pokemons found")
        return pokemons
