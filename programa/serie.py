import programa

class Serie(programa.Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

        self.tratamento_temporadas()

    def __str__(self):
        return f'{super().__str__()} | Temporadas: {self.temporadas}'


    def tratamento_temporadas(self):
        if not isinstance(self.temporadas, int):
            raise ValueError('As temporadas devem ser inteiros!')
        return self.temporadas