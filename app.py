from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from models import Roteiro
from logger import logger
from schemas import *
from flask_cors import CORS
import requests
import json


info = Info(title="Minha API para buscar roteiro de viagem no CHATGPT", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
roteiro_tag = Tag(name="Roteiro", description="Busca roteiro de viagens no CHATGPT pelo nome da cidade")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/busca_roteiro', tags=[roteiro_tag],
         responses={"200": RoteiroBuscaPorCidadeSchema, "404": ErrorSchema})
def busca_roteiro(query: RoteiroBuscaPorCidadeSchema):
    """Faz a busca por viagem através do nome da cidade.

    Retorna uma representação das viagens e roteiros associados.
    """
    termo = unquote(query.cidade)
    logger.info(f"Buscando o roteiro da cidade: {termo}")
    
    """ Chamando o CHATGPT"""

    roteiro = busca_roteiro_chatGPT(query.qtd_dias, termo)
 
    return apresenta_roteiro (roteiro)


