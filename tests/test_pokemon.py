from unittest.mock import patch

import pytest

from db import db
from models.ability import AbilityModel
from models.pokemon import PokemonModel


@patch("resources.pokemon.requests.get")
def test_pokemon_abilities_order(mock_get, client):
    # Simulando a resposta da PokéAPI com habilidades desordenadas
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "abilities": [
            {"ability": {"name": "static"}},
            {"ability": {"name": "lightning-rod"}},
        ]
    }

    # Fazendo a requisição ao endpoint para buscar o Pokémon pela PokéAPI
    response = client.get("/pokemon/pikachu")

    # Verificando o status da resposta
    assert response.status_code == 202

    # Verificando se as habilidades retornadas estão em ordem alfabética
    abilities_response = response.json["abilities"]
    assert abilities_response == sorted(abilities_response)

    # Verificando se as habilidades foram salvas no banco em ordem alfabética
    with client.application.app_context():
        abilities_in_db = [
            ability.name
            for ability in AbilityModel.query.order_by(AbilityModel.name).all()
        ]
        assert abilities_in_db == sorted(abilities_in_db)
