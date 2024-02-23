import os
import filme
import serie
import playlist
import programa

class Menu:

    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def cadastrar_filme():
        try:
            nome = input('Digite o nome do Filme: ')
            ano = int(input('Digite o ano do Filme: '))
            duracao = int(input('Digite a duração do Filme (em minutos): '))
            return filme.Filme(nome, ano, duracao)
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número inteiro.")
            return None

    @staticmethod
    def cadastrar_serie():
        try:
            nome = input('Digite o nome da Série: ')
            ano = int(input('Digite o ano da Série: '))
            temporadas = int(input('Digite a quantidade de Temporadas: '))
            return serie.Serie(nome, ano, temporadas)
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número inteiro.")
            return None

    @staticmethod
    def adicionar_programa():
        while True:
            try:
                print('Digite 1 para Filme e 2 para Série: ')
                op = int(input('[1]- Filme | [2]- Série: '))

                if op == 1:
                    print('Cadastrando Filmes!')
                    filme = Menu.cadastrar_filme()
                    if filme:
                        programa.Programa.filmes_e_series.append(filme)
                        print(f'Filme "{filme.nome}" cadastrado com sucesso!')
                        return False

                elif op == 2:
                    print('Cadastrando Séries!')
                    serie = Menu.cadastrar_serie()
                    if serie:
                        programa.Programa.filmes_e_series.append(serie)
                        print(f'Série "{serie.nome}" cadastrada com sucesso!')
                        return False
                else:
                    print('Opção inválida, saindo!')
                    break

            except Exception as e:
                print(f"Erro inesperado: {e}")
    @staticmethod
    def criar_playlist():
        while True:
            try:
                nome_playlist = input('Digite o nome da nova playlist: ')
                nova_playlist = playlist.Playlist(nome_playlist, programa.Programa.filmes_e_series)
                print(f'Nova playlist cadastrada com sucesso: {nova_playlist}')
                return nova_playlist

            except ValueError as e:
                print(f'Erro: {e}, tente novamente')

    @staticmethod
    def listar_tudo():
        print('Listando os programas salvos: ')
        programa.Programa.listar_programas()

    @classmethod
    def listar_playlist_por_nome(cls, lista_playlists, nome_playlist):
        playlists_encontradas = []

        for playlist in lista_playlists:
            if playlist.nome_playlist == nome_playlist:
                playlists_encontradas.append(playlist)

        if not playlists_encontradas:
            print(f'Nenhuma playlist encontrada com o nome "{nome_playlist}".')
        else:
            print(f'Playlists encontradas com o nome "{nome_playlist}":')
            for playlist in playlists_encontradas:
                print(f'- {playlist.nome_playlist}')


    def main():
        playlist_do_dia = playlist.Playlist('Fim de semana', programa.Programa.filmes_e_series)
        playlists = [playlist_do_dia]

        while True:
            print("\nMenu:")
            print("1. Adicionar Programa")
            print("2. Listar Programas")
            print("3. Listar Playlist por Nome")
            print("4. Criar Nova Playlist")
            print("0. Sair")

            opcao = int(input('Escolha uma opção: '))

            if opcao == 1:
                Menu.adicionar_programa()
            elif opcao == 2:
                Menu.listar_tudo()
            elif opcao == 3:
                nome_playlist = input('Digite o nome da playlist: ')
                Menu.listar_playlist_por_nome(playlists, nome_playlist)
            elif opcao == 4:
                nova_playlist = Menu.criar_playlist()
                playlists.append(nova_playlist)
                print(f'Playlist "{nova_playlist.nome_playlist}" criada com sucesso!')
            elif opcao == 0:
                print('Saindo do programa.')
                break
            else:
                print('Opção inválida, tente novamente.')


if __name__ == "__main__":
    Menu.main()
