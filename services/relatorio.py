from utils.arquivo import carregar_reservas
from utils.validacoes import validar_cpf

def exibir_menu_relatorio():
    menu = """
    ----- OPÇÕES DE RELATÓRIO -----
    1 - Reservas com status R (Reservado)
    2 - Reservas com status C (Cancelado)
    3 - Reservas com status A (Ativo)
    4 - Reservas com status F (Finalizado)
    5 - Valor total recebido (status F)
    6 - Relatório por CPF
    """
    return menu

def filtrar_por_status(status_alvo):
    reservas = carregar_reservas()
    filtradas = [r for r in reservas if r.status == status_alvo]
    
    if not filtradas:
        print(f"Nenhuma reserva com status {status_alvo}.")
        return

    print(f"\n>>> Relatório de reservas com status '{status_alvo}':")
    for r in filtradas:
        print(f"ID: {r.id} | CPF: {r.cpf} | Quarto: {r.tipo_quarto} | Dias: {r.dias} | Valor: R${r.valor}")
    print(f">>> Total: {len(filtradas)} reserva(s).")

def relatorio_valor_total_finalizado():
    reservas = carregar_reservas()
    total = sum(r.valor for r in reservas if r.status == 'F')
    print(f"\n>>> Valor total recebido por reservas finalizadas: R${total}")

def relatorio_por_cpf():
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

    print(f"\n>>> Relatório de reservas para o CPF {cpf}:")
    for r in reservas_do_cpf:
        print(f"ID: {r.id} | Status: {r.status} | Quarto: {r.tipo_quarto} | Dias: {r.dias} | Valor: R${r.valor}")
    print(f">>> Total: {len(reservas_do_cpf)} reserva(s).")

def executar_relatorio():
    print(exibir_menu_relatorio())
    opcoes = ["1", "2", "3", "4", "5", "6"]

    while True:
        escolha = input("Escolha uma opção de relatório: ").strip()
        if escolha in opcoes:
            break
        print("Opção inválida.")

    if escolha == "1":
        filtrar_por_status("R")
    elif escolha == "2":
        filtrar_por_status("C")
    elif escolha == "3":
        filtrar_por_status("A")
    elif escolha == "4":
        filtrar_por_status("F")
    elif escolha == "5":
        relatorio_valor_total_finalizado()
    elif escolha == "6":
        relatorio_por_cpf()
