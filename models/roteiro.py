class Roteiro:

       def __init__(self, cidade, qtd_dias, roteiro):
        """
        Cria uma viagem

        Arguments:
            cidade: local da viagem ( estamos restringindo apenas para cidades brasileiras)
            qtd_dias: duração da viagem em dias
        """
        self.cidade = cidade
        self.qtd_dias = qtd_dias
        self.roteiro = roteiro
       

