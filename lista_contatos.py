# Valida se digitou um número
def validar_escolha(decisao):
    try:
        validar = int(decisao)
        return validar

    except Exception:
        print("Opção inválida")

# Verifica se escolha está entre as opções disponíveis
def verifica_opcao_escolhida(contatos, opcao):
    if opcao >= 1 and opcao <= len(contatos):
        opcao -= 1
        return opcao



def adicionar_contato(nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone,
               "email": email, 'favoritos': False}
    contatos.append(contato)
    return


def ver_contatos(contatos):
    print('\nLista de contatos')
    for index, contato in enumerate(contatos, start=1):
        favoritos = "Sim" if contato['favoritos'] else "Não"
        print(
            f'{index} - {contato['nome']} -  {contato['telefone']} - {contato['email']} - Favoritos: [{favoritos}] ')


def editar_contato(contatos, opcao):
    opcao = verifica_opcao_escolhida(contatos, opcao)

    novo_nome = input("Digite o nome: ")
    novo_telefone = input("Digite o telefone: ")
    novo_email = input("Digite o email: ")
    favoritos = "Sim" if contatos[opcao]['favoritos'] else "Não"

    print(
        f'\nO contato Nome: {contatos[opcao]['nome']} - telefone {contatos[opcao]['telefone']} -', end=''
        f'Email: {contatos[opcao]['email']} - Favorito [{favoritos}] foi editado')

    contatos[opcao]['nome'] = novo_nome
    contatos[opcao]['telefone'] = novo_telefone
    contatos[opcao]['email'] = novo_email

    print(f' para:\n Nome: {contatos[opcao]['nome']} - Telefone:{contatos[opcao]['telefone']} - '
          f'Email: {contatos[opcao]['email']} - Favorito [{favoritos}]')


def adicioar_favorito(contatos, opcao_escolhida):
    opcao_escolhida = verifica_opcao_escolhida(contatos, opcao_escolhida)

    # Remove dos favoritos se já estiver em "favoritos"
    if contatos[opcao_escolhida]['favoritos']:
        contatos[opcao_escolhida]['favoritos'] = False
        print(
            f"Contato {contatos[opcao_escolhida]['nome']} remvido de favoritos")
        return

    contatos[opcao_escolhida]['favoritos'] = True
    print(
        f"Contato {contatos[opcao_escolhida]['nome']} foi adicionado aos favoritos")


def ver_favoritos(contatos: list):
    print("Lista de contatos favoritos")
    for index, contato in enumerate(contatos):
        if contato['favoritos']:
            print(
                f'None: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']}')


def deletar_contato(contatos, opcao_escolhida):
    opcao_escolhida = verifica_opcao_escolhida(contatos, opcao_escolhida)

    print(
        f' O contato None: {contatos[opcao_escolhida]['nome']} - Telefone: {contatos[opcao_escolhida]['telefone']} - Email: {contatos[opcao_escolhida]['email']} ', end=''
        f'foi removido')
    contatos.remove(contatos[opcao_escolhida])


contatos = []
while True:
    print("\nAgenda de contatos")
    print("1 - Adiconar contato ")
    print("2 - Ver contatos ")
    print("3 - Editar Contato ")
    print("4 - Adicionar/Remover contatos de favoritos")
    print("5 - Ver contatos favoritos")
    print("6 - Excluir contato")
    print("7 - Sair")

    escolha = int(input("Digite uma opção que deseja realizar: "))
    validar_escolha(escolha)

    if escolha == 1:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(nome, telefone, email)

    elif escolha == 2:
        ver_contatos(contatos)

    elif escolha == 3:
        ver_contatos(contatos)
        opcao = input("Escolha um contato para editar\n")
        editar_contato(contatos, validar_escolha(opcao))

    elif escolha == 4:
        ver_contatos(contatos)
        escolha = input(
            "Escolha um contato para adicionar/remover de favoritos ")
        adicioar_favorito(contatos, validar_escolha(escolha))

    elif escolha == 5:
        ver_favoritos(contatos)

    elif escolha == 6:
        ver_contatos(contatos)
        escolha = input("Escolha qual contato deseja excluir: ")
        deletar_contato(contatos, validar_escolha(escolha))

    elif escolha == 7:
        break


print("Programa Finalizado ")
