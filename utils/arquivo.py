from models.reserva import Reserva

def carregar_reservas():
    try:
        with open("reservas.txt", "r") as arq:
            return [Reserva.from_csv(linha) for linha in arq.readlines()]
    except FileNotFoundError:
        return []

def salvar_reservas(lista):
    with open("reservas.txt", "w") as arq:
        arq.writelines([reserva.to_csv() for reserva in lista])
