from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("Pokémons", "pokemons", description="Operations on pokemons")

# @blp.route("/")
# class Pokemon(MethodView):
