import requests

from .models import Personagem, montar_personagem


class PersonagemNaoEncontrado(Exception):
    pass


def buscar_personagem(nome: str) -> Personagem:
    resposta = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}",
        timeout=10,
    )
    if resposta.status_code == 404:
        raise PersonagemNaoEncontrado
    resposta.raise_for_status()
    return montar_personagem(resposta.json())