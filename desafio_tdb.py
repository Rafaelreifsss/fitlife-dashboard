# Simulando nosso "Banco de Dados" em memória
fila_jovens = [
    {"id": 1, "nome": "Lucas Silva", "regiao": "São Paulo - SP", "apadrinhado": False},
    {"id": 2, "nome": "Mariana Santos", "regiao": "Rio de Janeiro - RJ", "apadrinhado": False},
    {"id": 3, "nome": "Pedro Henrique", "regiao": "Salvador - BA", "apadrinhado": False}
]

lista_doadores = []


def processar_doacao(nome_doador, email_doador, valor, regiao_desejada):
    """
    Função que processa a doação de pessoa física e tenta fazer o match
    com um jovem da fila de atendimento da mesma região.
    """
    print(f"\n--- Processando doação de {nome_doador} (R$ {valor:.2f}) ---")

    # 1. Registra o doador
    novo_doador = {
        "id": len(lista_doadores) + 1,
        "nome": nome_doador,
        "email": email_doador,
        "valor": valor,
        "regiao": regiao_desejada
    }
    lista_doadores.append(novo_doador)

    # 2. Algoritmo de Match: Procura um jovem na mesma região sem padrinho
    jovem_encontrado = None
    for jovem in fila_jovens:
        if jovem["regiao"] == regiao_desejada and not jovem["apadrinhado"]:
            jovem_encontrado = jovem
            break  # Encontrou o primeiro compatível, para a busca

    # 3. Resultado do Apadrinhamento
    if jovem_encontrado:
        jovem_encontrado["apadrinhado"] = True
        print(f"Sucesso! Doação confirmada.")
        print(
            f"🔗 MATCH REALIZADO: {nome_doador} agora apadrinha o(a) jovem {jovem_encontrado['nome']} ({jovem_encontrado['regiao']}).")
        print(f"📧 E-mail de boas-vindas disparado para: {email_doador} com a história do jovem.")
    else:
        print(f"Sucesso! Doação confirmada para o Fundo Geral da Turma do Bem.")
        print(
            f"ℹ️ Não havia jovens na fila exata da região '{regiao_desejada}' no momento, mas sua doação ajudará na expansão!")


# --- TESTANDO O CÓDIGO ---
if __name__ == "__main__":
    # Simulando uma doação de alguém de São Paulo
    processar_doacao(
        nome_doador="Ana Souza",
        email_doador="ana.souza@email.com",
        valor=20.00,
        regiao_desejada="São Paulo - SP"
    )

    # Simulando outra doação de alguém do Rio de Janeiro
    processar_doacao(
        nome_doador="Carlos Lima",
        email_doador="carlos.lima@email.com",
        valor=35.00,
        regiao_desejada="Rio de Janeiro - RJ"
    )