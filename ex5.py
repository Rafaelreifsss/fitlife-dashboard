idade = int(input("Digite sua idade: "))

match idade:
    case x if x > 18:
        print("Maior de idade")
    case x if x < 18:
        print("Menor de idade")
    case _:
        print("Valor inavalido")