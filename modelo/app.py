import cadastrar
import pessoa
def main():

    cadastro = cadastrar.Cadastrar()

    while True:
        cadastrar.Cadastrar.menu()
        escolha = input("Escolha uma opção (0-4): ")

        if escolha == "0":
            print("Saindo do programa.")
            break
        elif escolha == "1":
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            nova_pessoa = pessoa.Pessoa(nome, idade)
            cadastro.adicionar_pessoa(nova_pessoa)
        elif escolha == "2":
            nome = input("Digite o nome da pessoa a ser removida: ")
            cadastro.remover_pessoa(nome)
        elif escolha == "3":
            nome = input("Digite o nome da pessoa a ser atualizada: ")
            nova_idade = int(input("Digite a nova idade: "))
            cadastro.atualizar_pessoa(nome, nova_idade)
        elif escolha == "4":
            cadastro.mostrar_lista()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()