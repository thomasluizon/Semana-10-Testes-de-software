def converte(numeroEmRomano):
    tabela = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    acumulador = 0
    ultimovizinhodireita = 0
    for i in reversed(range(len(numeroEmRomano))):
        atual = 0
        numCorrente = numeroEmRomano[i]
        if numCorrente in tabela:
            atual = tabela[numCorrente]

        if atual < ultimovizinhodireita:
            multiplicador = -1
        else:
            multiplicador = 1

        acumulador += atual * multiplicador
        ultimovizinhodireita = atual

    return acumulador
