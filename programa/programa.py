import playlist
from datetime import datetime

class Programa(playlist.Playlist):
    filmes_e_series = []

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano

        self.valida_nome()
        self.tratamento_de_ano()

        Programa.filmes_e_series.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self._ano}'

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def tratamento_de_nome(self):
        if not isinstance(self.nome, str):
            raise ValueError('O Nome deve ser uma string!')
        self._nome = self._nome.strip()

    def valida_nome(self):
        self.tratamento_de_nome()
        if not self.nome:
            raise ValueError('O nome esta vazio!')

    def tratamento_de_ano(self):
        data_atual = datetime.now().year
        if self._ano < 1930 or self._ano > data_atual:
            raise ValueError(f"Ano inválido. Deve estar entre 1930 e {data_atual}.")
        return f"Ano {self._ano} é válido."

    @staticmethod
    def listar_programas():
        playlist_de_dia = playlist.Playlist('Fim de semana', Programa.filmes_e_series)
        for programa in playlist_de_dia:
            detalhes = programa.duracao if hasattr(programa, 'duracao') else getattr(programa, 'temporadas', None)
            print(programa)
