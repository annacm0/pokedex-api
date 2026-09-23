from dataclasses import dataclass


@dataclass
class Personagem:
    nome: str
    altura: int
    peso: int
    tipos: list[str]


def montar_personagem(dados_json: dict) -> Personagem:
    return Personagem(
        nome=dados_json["name"],
        altura=dados_json["height"],
        peso=dados_json["weight"],
        tipos=[tipo["type"]["name"] for tipo in dados_json["types"]],
    )