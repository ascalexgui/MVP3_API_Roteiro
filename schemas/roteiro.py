from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional, List
from models.roteiro import Roteiro

from senha import API_KEY
import json
import requests


class RoteiroSchema(BaseModel):
    """ Define o roteiro de uma viagem 
    """
    roteiro : str = ""

class RoteiroBuscaPorCidadeSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da cidade para retornar o roteiro
    """
    cidade: str = "Rio de Janeiro"
    qtd_dias: int = "15"

def apresenta_roteiro(mensagem:any ):
    """ Retorna uma representação do roteiro seguindo o schema definido em
        RoteiroSchema.
    """
    return {
        "roteiro": mensagem
    }

def busca_roteiro_chatGPT (qtd_dias, cidade):

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": f"Roteiro de viagem de {qtd_dias} para {cidade}"}]
    }

    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data= body_mensagem)

    retornoGPT = requisicao.json()

    roteiro = retornoGPT["choices"][0]["message"]["content"]

    return roteiro


