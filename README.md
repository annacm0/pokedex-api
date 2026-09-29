# Pokédex API

API REST desenvolvida em **Python com FastAPI** para consulta de Pokémon por meio da [PokéAPI](https://pokeapi.co/).

## 🌐 API publicada

**API:**

https://pokedex-api-85l0.onrender.com

**Documentação interativa (Swagger):**

https://pokedex-api-85l0.onrender.com/docs

### Exemplo

```text
https://pokedex-api-85l0.onrender.com/personagens/pikachu
```

## 🚀 Sobre o projeto

A API recebe o nome de um Pokémon, consulta a PokéAPI e retorna informações selecionadas sobre ele.

Os dados disponibilizados são:

* Nome
* Altura
* Peso
* Tipos

### Exemplo de resposta

```json
{
  "nome": "pikachu",
  "altura": 4,
  "peso": 60,
  "tipos": ["electric"]
}
```

## 🛠️ Tecnologias

* **Python**
* **FastAPI**
* **Uvicorn**
* **Requests**
* **Pytest**
* **HTTPX**
* **PokéAPI**
* **Git e GitHub**
* **Render**

## 📁 Estrutura do projeto

```text
pokedex-api/
├── app/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── main.py
│   ├── models.py
│   └── pokeapi.py
│
├── tests/
│   ├── __init__.py
│   └── test_personagens.py
│
├── .gitignore
├── Procfile
├── README.md
├── pytest.ini
├── render.yaml
└── requirements.txt
```

### Organização

* `main.py` — define os endpoints da API e o tratamento das exceções.
* `models.py` — define o modelo `Personagem` e transforma os dados recebidos da PokéAPI.
* `pokeapi.py` — realiza a comunicação com a PokéAPI.
* `exceptions.py` — contém a exceção personalizada `PersonagemNaoEncontrado`.
* `tests/` — contém os testes automatizados.
* `Procfile` — define o comando de inicialização da aplicação.
* `render.yaml` — contém a configuração do serviço para publicação no Render.

## ⚙️ Executando localmente

### 1. Clone o repositório

```bash
git clone https://github.com/annacm0/pokedex-api.git

cd pokedex-api
```

### 2. Crie o ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

A API ficará disponível localmente em:

```text
http://127.0.0.1:8000
```

A documentação interativa do FastAPI estará disponível em:

```text
http://127.0.0.1:8000/docs
```

## 🔎 Endpoints

### Página inicial

```http
GET /
```

Retorna uma mensagem de boas-vindas e o caminho da documentação da API.

### Buscar personagem

```http
GET /personagens/{nome}
```

Exemplo:

```text
GET /personagens/pikachu
```

Ou diretamente na API publicada:

```text
https://pokedex-api-85l0.onrender.com/personagens/pikachu
```

### Resposta de sucesso

**200 OK**

```json
{
  "nome": "pikachu",
  "altura": 4,
  "peso": 60,
  "tipos": ["electric"]
}
```

### Personagem não encontrado

Quando o Pokémon informado não existe:

**404 Not Found**

```json
{
  "detail": "Personagem 'pokemon-que-nao-existe' não encontrado na Pokédex."
}
```

### Serviço externo indisponível

Quando ocorre uma falha na comunicação com a PokéAPI:

**503 Service Unavailable**

```json
{
  "detail": "Serviço de personagens indisponível no momento."
}
```

## 🧪 Testes

O projeto utiliza **Pytest** para testes automatizados.

Para executar:

```bash
pytest
```

Testes implementados:

* consulta de um personagem existente;
* consulta de um personagem inexistente.

Resultado:

```text
2 passed
```

## ☁️ Publicação

A aplicação está publicada utilizando o **Render**.

A configuração de publicação está definida nos arquivos:

```text
Procfile
render.yaml
```

**API publicada:**

https://pokedex-api-85l0.onrender.com

**Documentação interativa:**

https://pokedex-api-85l0.onrender.com/docs

> A instância gratuita do Render pode entrar em estado de inatividade após um período sem requisições. Nesse caso, a primeira requisição pode levar alguns segundos para responder.

## 📚 Conceitos praticados

Durante o desenvolvimento foram praticados:

* desenvolvimento de APIs REST com FastAPI;
* criação de endpoints;
* consumo de APIs externas;
* tratamento de exceções;
* modelagem de dados;
* testes automatizados;
* organização de projetos Python;
* ambientes virtuais;
* Git e GitHub;
* branches e Pull Requests;
* preparação e configuração para deploy;
* publicação de uma API em ambiente de nuvem.

---

Projeto desenvolvido durante o desafio **#7DaysOfCode — Vibe Coding com Claude Code**, da Alura, com foco na construção de uma API, consumo de serviço externo, tratamento de erros, testes automatizados e publicação em ambiente de nuvem.




