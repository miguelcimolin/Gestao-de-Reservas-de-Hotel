def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def validar_numero(numero):
    return numero.isdigit() and int(numero) > 0
