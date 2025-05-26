def calcular_valor(pessoas, tipo_quarto, dias):
    precos = {"S": 100, "D": 200, "P": 300}
    return pessoas * precos.get(tipo_quarto, 0) * dias
