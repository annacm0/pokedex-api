from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_obter_pikachu():
    resposta = client.get("/personagens/pikachu")

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "pikachu"


def test_obter_personagem_inexistente():
    resposta = client.get("/personagens/personagem-inexistente")

    assert resposta.status_code == 404
