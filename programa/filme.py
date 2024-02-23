import programa

class Filme(programa.Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        self.tratamento_duracao()

    def __str__(self):
        return f'{super().__str__()} | Duração: {self.tratamento_de_tempo()}'

    def tratamento_de_tempo(self):
        horas = self.duracao // 60
        minutos = self.duracao % 60
        return f'{horas}h e {minutos}min'

    def tratamento_duracao(self):
        if not isinstance(self.duracao, int):
            raise ValueError('A duração deve ser um inteiro!')
        return self.duracao
