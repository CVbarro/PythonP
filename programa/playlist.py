class Playlist:
    def __init__(self, nome_playlist, programas):
        self.nome_playlist = nome_playlist
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

    def listagem_de_playlist(self):
        print(f'\nListando programas da playlist "{self.nome_playlist}":')
        for programa in self._programas:
            print(programa)
