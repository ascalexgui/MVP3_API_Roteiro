# Aluno: Andréia Souza Carvalho
Entrega do MVP 3
Disciplina **Desenvolvimento Full Stack Avançado** 

API em REST : ROTEIRO

Este pequeno projeto faz parte da entrega do MVP da Disciplina **Desenvolvimento Full Stack Avançado** 

API implementada seguindo o estilo REST.

ATENÇÂO: Esta API faz uso do CHATGPT logo precisamos de uma chave API_KEY que está armazenada no arquivo senha.py.
O arquivo com essa API_KEY será enviado separadamente e deverá ser substituido antes de executar o projeto.

---
### Instalação

### Instruções para instalação do ambiente

Acessar a WSL

## Ativar o Docker

sudo service docker start

# Ir para o diretório do projeto MVP_Viagem_ASC onde se encontra o arquivo dockerfile 
1) cd '/mnt/c/Users/cyl7/OneDrive - PETROBRAS/Documents/posgraduacao_PUC/sprint_03/MVP_VIagem_ASC$'

# Fazer o build da primeira imagem - Imagem da Viagem
2)docker build -t img-viagem .

# Ir para o diretório do projeto MVP_Roteiro_ASC onde se encontra o arquivo dockerfile 
3) cd '/mnt/c/Users/cyl7/OneDrive - PETROBRAS/Documents/posgraduacao_PUC/sprint_03/MVP_Roteiro_ASC$'

# Fazer o build da segunda imagem - Imagem da Viagem do Roteiro
4) docker build -t img-roteiros .

# Verificar se as imagens foram geradas com sucesso
5) docker images
 
# Criar a rede para conexão dos dois containers
docker network create ponte_docker -d bridge
 
# Executar o primeiro container
docker run -p 5001:5001 --name cntn-viagem2 --network ponte_docker img-viagem
 
# Executar o segundo container
docker run -p 5000:5000 --name servico-roteiro --network ponte_docker img-roteiros

