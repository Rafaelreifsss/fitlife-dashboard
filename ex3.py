dia = int(input("Digite um dia da semana (1 até 7): "))

match dia:
    case 7 | 1:
       print("Final de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil")