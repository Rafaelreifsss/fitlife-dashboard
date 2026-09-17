dia = input("Digite o  dia da semana")

#função lower: transforma texto em minusculo

match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("dia útil")
    case "sabado" | "domingo":
        print("Final de semana")


if dia == "segunda" or dia == "terça" or dia == "quarta" or dia == "quinta" or dia == "sexta":
    print("Dia útil")
elif dia == "sabado" or dia == "domingo":
    print("Final de semana")
else:
    print("Dia invalido")