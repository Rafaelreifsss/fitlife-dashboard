opcao = int(input("Digite uma opcao (0 até 3): "))

# A estrutura match-case por padrão compara valores por igualdade
# Em outras linguagens é conhecido como SWITCH-CASE
# No match informamos a varíavel que será verificada, no nosso caso é "opção"
match opcao:
    case 0:
        print("opcao 0")
    case 1:
        print("opcao 1")
    case 2:
        print("opcao 2")
    case 3:
        print("opcao 3")
    case _:
        print("Valor incorreto. Digite de 0 até 3")


#OU

if opcao == 0:
    print("opcao 0")
elif opcao == 1:
    print("opcao 1")
elif opcao == 2:
    print("opcao 2")
elif opcao == 3:
    print("opcao 3")
else:
    print("Valor incorreto. Digite de 0 até 3")