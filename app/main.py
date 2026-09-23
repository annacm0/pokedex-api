import requests
from fastapi import FastAPI, HTTPException

from .models import Personagem
from .pokeapi import PersonagemNaoEncontrado, buscar_personagem

app = FastAPI()


@app.get("/personagens/{nome}", response_model=Personagem)
def obter_personagem(nome: str) -> Personagem:
	try:
		return buscar_personagem(nome)
	except PersonagemNaoEncontrado:
		raise HTTPException(
			status_code=404,
			detail=f"Personagem '{nome}' não encontrado na Pokédex.",
		)
	except requests.RequestException:
		raise HTTPException(
			status_code=503,
			detail="Serviço de personagens indisponível no momento.",
		)