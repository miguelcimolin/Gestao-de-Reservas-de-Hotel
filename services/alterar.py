from utils.arquivo import carregar_reservas, salvar_reservas
from utils.validacoes import validar_cpf, validar_numero
from utils.calculos import calcular_valor

def executar_alteracao():
    reservas = carregar_reservas()

    while True:
        cpf = input("Digite o CPF (somente números): ").strip()
        if validar_cpf(cpf):
            break
        print("CPF inválido.")

    reservas_do_cpf = [r for r in reservas if r.cpf == cpf]
    if not reservas_do_cpf:
        print("Nenhuma reserva encontrada para este CPF.")
        return

    print("\n>>> Reservas encontradas:")
    for r in reservas_do_cpf:
        print(f"ID: {r.id} | Titular: {r.titular} | Quarto: {r.tipo_quarto} | Dias: {r.dias} | Pessoas: {r.pessoas} | Valor: R${r.valor} | Status: {r.status}")

    ids_validos = [str(r.id) for r in reservas_do_cpf]
    while True:
        id_escolhido = input("Digite o ID da reserva a ser alterada: ").strip()
        if id_escolhido in ids_validos:
            break
        print("ID inválido.")

    reserva_alvo = next(r for r in reservas if str(r.id) == id_escolhido)

    menu = """
    O que deseja alterar?
    1 - Número de pessoas
    2 - Tipo do quarto
    3 - Número de dias
    4 - Status
    """
    opcoes_validas = ["1", "2", "3", "4"]
    while True:
        opcao = input(menu + "\nEscolha: ").strip()
        if opcao in opcoes_validas:
            break
        print("Opção inválida.")

    if opcao == "1":
        while True:
            novo_valor = input("Novo número de pessoas: ")
            if validar_numero(novo_valor):
                novo_valor = int(novo_valor)
                if novo_valor != reserva_alvo.pessoas:
                    reserva_alvo.pessoas = novo_valor
                    break
            print("Valor inválido ou igual ao atual.")
        reserva_alvo.valor = calcular_valor(reserva_alvo.pessoas, reserva_alvo.tipo_quarto, reserva_alvo.dias)

    elif opcao == "2":
        tipos_validos = ["S", "D", "P"]
        while True:
            novo_quarto = input("Novo tipo de quarto (S, D, P): ").strip().upper()
            if novo_quarto in tipos_validos and novo_quarto != reserva_alvo.tipo_quarto:
                reserva_alvo.tipo_quarto = novo_quarto
                break
            print("Tipo inválido ou igual ao atual.")
        reserva_alvo.valor = calcular_valor(reserva_alvo.pessoas, reserva_alvo.tipo_quarto, reserva_alvo.dias)

    elif opcao == "3":
        while True:
            novos_dias = input("Novo número de dias: ")
            if validar_numero(novos_dias):
                novos_dias = int(novos_dias)
                if novos_dias != reserva_alvo.dias:
                    reserva_alvo.dias = novos_dias
                    break
            print("Valor inválido ou igual ao atual.")
        reserva_alvo.valor = calcular_valor(reserva_alvo.pessoas, reserva_alvo.tipo_quarto, reserva_alvo.dias)

    elif opcao == "4":
        status_validos = ["R", "A", "F", "C"]
        while True:
            novo_status = input("Novo status (R, A, F, C): ").strip().upper()
            if novo_status in status_validos and novo_status != reserva_alvo.status:
                reserva_alvo.status = novo_status
                break
            print("Status inválido ou igual ao atual.")

    salvar_reservas(reservas)
    print(">>> Alteração realizada com sucesso!")
