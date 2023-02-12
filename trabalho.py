def resumo():
    mensagem = "\nAlan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = "\nPhD no Departamento de Matemática de Princeton."
    return mensagem


def contribuicoes():
    mensagem = "\nDesenvolvimento da moderna ciência da computação teórica, formalizando os conceitos de algoritmo e computação com a máquina de Turing, que pode ser considerada um modelo de um computador de uso geral."
    return mensagem


def artigos():
    mensagem = "\nArtigo sobre as bases químicas da morfogênese\n Artigo Sobre números computáveis, com uma Aplicação ao Entscheidungsproblem\n Antigo As Aplicações da Probabilidade à Criptografia\n Artigo sobre Estatísticas de Repetições."
    return mensagem


def citacoes():
    mensagem = "\nIf a machine is expected to be infallible, it cannot also be intelligent.\n Can machines think?"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)