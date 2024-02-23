import pessoa

class Cadastrar:
    def __init__(self):
        self.lista_pessoas = []
        self._cadastrado = False

    def adicionar_pessoa(self, pessoa):
        self.lista_pessoas.append(pessoa)

    def mostrar_lista(self):
        if not self.lista_pessoas:
            print("Lista de Pessoas está vazia.")
        else:
            print("\nLista de Pessoas:")
            for pessoa in self.lista_pessoas:
                print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

    def remover_pessoa(self, nome):
        for pessoa in self.lista_pessoas:
            if  pessoa.nome ==  nome:
                print("Pessoa encontrada, removendo-a!")
                self.lista_pessoas.remove(pessoa)
                print(f'Pessoa: {pessoa.nome} removida com sucesso!')
                return
            else:
                print('Pessoa não encontrada !')

    def atualizar_pessoa(self, nome, nova_idade):
        for pessoa in self.lista_pessoas:
            if pessoa.nome == nome:
                pessoa.idade = nova_idade
                print(f"Idade de {pessoa.nome} atualizada para {nova_idade}.")
                return
        print(f"{nome} não encontrado(a) na lista.")

    @property
    def cadastrado(self):
        return 'Cadastrado' if self._cadastrado else 'Não cadastrado'

    def ativar_cadastro(self):
        self._cadastrado = not self._cadastrado

    def menu():
        print("\nMenu:")
        print("1. Adicionar Pessoa")
        print("2. Remover Pessoa")
        print("3. Atualizar Idade")
        print("4. Mostrar Lista")
        print("0. Sair")
