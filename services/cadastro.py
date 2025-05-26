# services/cadastro.py
from models.reserva import Reserva
from utils.arquivo import carregar_reservas, salvar_reservas
from utils.calculos import calcular_valor
from utils.validacoes import validar_nome, validar_cpf, validar_numero

def executar_cadastro():
    print('-'*50)
    print('A seguir, preencha as informações para realizar o cadastro.')

    reservas = carregar_reservas()
    novo_id = max([r.id for r in reservas], default=0) + 1

    while True:
        titular = input('Nome do titular: ').strip().upper().replace(' ', '')
        if validar_nome(titular):
            break
        print("Nome inválido.")

    while True:
        cpf = input('CPF (somente números): ').strip()
        if validar_cpf(cpf):
            break
        print("CPF inválido.")

    while True:
        pessoas = input('Quantas pessoas irão? ')
        if validar_numero(pessoas):
            pessoas = int(pessoas)
            break
        print("Número inválido.")

    opcoes_quarto = {"S": 100, "D": 200, "P": 300}
    while True:
        print("""
        -----TIPOS DE QUARTO-----
        | S - Standard (R$100 por pessoa)
        | D - Deluxe   (R$200 por pessoa)
        | P - Premium  (R$300 por pessoa)
        """)
        tipo_quarto = input("Tipo de quarto: ").strip().upper()
        if tipo_quarto in opcoes_quarto:
            break
        print("Tipo inválido.")

    while True:
        dias = input('Quantos dias? ')
        if validar_numero(dias):
            dias = int(dias)
            break
        print("Número de dias inválido.")

    valor = calcular_valor(pessoas, tipo_quarto, dias)
    nova_reserva = Reserva(novo_id, titular, cpf, pessoas, tipo_quarto, dias, valor, 'R')
    reservas.append(nova_reserva)
    salvar_reservas(reservas)
    print('-'*50)
    print('>>>Cadastro realizado com sucesso!')