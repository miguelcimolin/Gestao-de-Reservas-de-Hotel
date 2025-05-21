from utils.arquivo import carregar_reservas, salvar_reservas
from utils.validacoes import validar_cpf
from models.reserva import Reserva

def executar_checkin():
    reservas = carregar_reservas()

    while True:
        cpf = input("Digite o CPF (somente números): ").strip()
        if validar_cpf(cpf):
            break
        print("CPF inválido.")

    reservas_disponiveis = [r for r in reservas if r.cpf == cpf and r.status == 'R']
    
    if not reservas_disponiveis:
        print("Nenhuma reserva disponível para check-in com esse CPF.")
        return

    print("\n>>> Reservas disponíveis para check-in:")
    for r in reservas_disponiveis:
        print(f"ID: {r.id} | Titular: {r.titular} | Quarto: {r.tipo_quarto} | Dias: {r.dias} | Valor: R${r.valor}")

    ids_validos = [str(r.id) for r in reservas_disponiveis]
    while True:
        escolha = input("Digite o ID da reserva para realizar o check-in: ").strip()
        if escolha in ids_validos:
            break
        print("ID inválido.")

    for r in reservas:
        if str(r.id) == escolha:
            r.status = 'A'
            break

    salvar_reservas(reservas)
    print(">>> Check-in realizado com sucesso!")
