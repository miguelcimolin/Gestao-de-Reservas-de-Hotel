from utils.arquivo import carregar_reservas, salvar_reservas
from utils.validacoes import validar_cpf

def executar_checkout():
    reservas = carregar_reservas()

    while True:
        cpf = input("Digite o CPF (somente números): ").strip()
        if validar_cpf(cpf):
            break
        print("CPF inválido.")

    reservas_ativas = [r for r in reservas if r.cpf == cpf and r.status == 'A']
    
    if not reservas_ativas:
        print("Nenhuma reserva ativa para este CPF.")
        return

    print("\n>>> Reservas disponíveis para check-out:")
    for r in reservas_ativas:
        print(f"ID: {r.id} | Titular: {r.titular} | Quarto: {r.tipo_quarto} | Dias: {r.dias} | Valor: R${r.valor}")

    ids_validos = [str(r.id) for r in reservas_ativas]
    while True:
        escolha = input("Digite o ID da reserva para realizar o check-out: ").strip()
        if escolha in ids_validos:
            break
        print("ID inválido.")

    for r in reservas:
        if str(r.id) == escolha:
            r.status = 'F'
            break

    salvar_reservas(reservas)
    print(">>> Check-out realizado com sucesso!")
