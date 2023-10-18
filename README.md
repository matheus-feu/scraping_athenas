[![wakatime](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/2f548181-c647-4f83-ae98-af537bbf5794.svg)](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/2f548181-c647-4f83-ae98-af537bbf5794)

<h2 align="center">  Scraping Athenas 🚀 </h2>

<p align="center">  Scraping de e-commerce com segurança JWT FastAPI. </p>


## 🧐 Sobre <a name = "sobre"></a>

Este projeto foi desenvolvido para o processo seletivo da empresa [Athenas](https://www.athenas.online). O objetivo é
criar um scraping de um e-commerce e disponibilizar os dados em uma API REST. Para isso, foi utilizado o
framework [FastAPI](https://fastapi.tiangolo.com/), que é um framework web assíncrono de alto desempenho, fácil de
aprender, rápido para codificar, pronto para produção.

A API utiliza-se do SQLAlchemy para realizar as operações no baco de dados e possui autenticação JWT para garantir a
segurança dos dados.

## 🚀 Tecnologias utilizadas <a name = "tecnologias-utilizadas"></a>

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-FF5722?style=flat-square&logo=sqlalchemy&logoColor=white)
![PyCharm](https://img.shields.io/badge/-PyCharm-000000?style=flat-square&logo=pycharm&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)

## 🏁 Executando o projeto <a name = "executando-o-projeto"></a>

### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Você instalou a versão mais recente do [Python](https://www.python.org/downloads/).
* Possuir um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)
  ou [PyCharm](https://www.jetbrains.com/pt-br/pycharm/).
* Ter o [Git](https://git-scm.com/) instalado para clonar o projeto.
*

#### 📁 Clonar o repositório

```bash
# Clone este repositório
git clone https://github.com/matheus-feu/scraping_athenas.git

# Entrar no diretório
cd scraping_athenas
````

#### 🐍 Criar e ativar o ambiente virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate.bat

# Linux
source venv/bin/activate
````

#### 📦 Instalar as dependências

```bash
# Instalar as dependências
pip install -r requirements.txt

# Instalar as dependências utilizando o poetry
poetry install
poetry shell
````

#### 🚀 Executando o projeto

```bash
# Criar as tabelas no banco de dados
python create_tables.py

# Executar o projeto no arquivo principal
python main.py
````

## 📌 Endpoints <a name = "endpoints"></a>

### 📦 Usuários

O fluxo de autenticação é feito utilizando o OAuth2PasswordBearer (OAuth2, password). Para isso, é necessário criar um
usuário e realizar o login.

#### 📝 Criar usuário

```bash
POST /api/v1/users/signup
````

Informar no corpo da requisição os dados do usuário:

```json
{
  "id": 0,
  "name": "string",
  "email": "user@example.com",
  "password": "string"
}
```

#### 📝 Login

```bash
POST /api/v1/users/login
````

Se autenticar com sucesso, será retornado o token JWT:

```json
{
  "access_token": "string"
}
```

OAuth2PasswordBearer (OAuth2, password):

* Se autenticar utilizando seu email cadastrado em `username` e passando a `password`, a API liberará o acesso aos
  endpoints que necessitam de autenticação.

![authorize](https://imgur.com/t2mEaWw.png)


### 📦 Produtos

#### 📝 Scraping Produtos

```bash
GET /api/v1/products/{category}
````

O scraping é feito utilizando a biblioteca [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) e a
biblioteca [Selenium](https://selenium-python.readthedocs.io/).

Necessário informar como parâmetro a categoria de quais produtos deseja realizar o scraping e então será retornado um
JSON com os dados dos produtos.

| Categoria   | Nome da Categoria |
|:------------|:------------------|
| `phones`    | Celulares         |
| `computers` | Computadores      |

- Exemplo de retorno com a categoria `computers`:

```json
[
  {
    "title": "Amazon Kindle",
    "image": "/images/test-sites/e-commerce/items/cart2.png",
    "link": "/test-sites/e-commerce/static/product/498",
    "price": "$103.99",
    "description": "6\" screen, wifi",
    "reviews": "3 reviews"
  },
  {
    "title": "iPad Mini Reti...",
    "image": "/images/test-sites/e-commerce/items/cart2.png",
    "link": "/test-sites/e-commerce/static/product/499",
    "price": "$537.99",
    "description": "Wi-Fi + Cellular, 32GB, Silver",
    "reviews": "8 reviews"
  },
  {
    "title": "IdeaTab A3500L",
    "image": "/images/test-sites/e-commerce/items/cart2.png",
    "link": "/test-sites/e-commerce/static/product/500",
    "price": "$88.99",
    "description": "Black, 7\" IPS, Quad-Core 1.2GHz, 8GB, Android 4.2",
    "reviews": "7 reviews"
  },
  {
    "title": "Galaxy Tab 3",
    "image": "/images/test-sites/e-commerce/items/cart2.png",
    "link": "/test-sites/e-commerce/static/product/507",
    "price": "$107.99",
    "description": "7\", 8GB, Wi-Fi, Android 4.2, Yellow",
    "reviews": "14 reviews"
  },
  {
    "title": "Memo Pad HD 7",
    "image": "/images/test-sites/e-commerce/items/cart2.png",
    "link": "/test-sites/e-commerce/static/product/508",
    "price": "$101.99",
    "description": "IPS, Dual-Core 1.2GHz, 8GB, Android 4.3",
    "reviews": "10 reviews"
  }
]
```


