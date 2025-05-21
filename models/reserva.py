class Reserva:
    def __init__(self, id, titular, cpf, pessoas, tipo_quarto, dias, valor, status):
        self.id = int(id)
        self.titular = titular
        self.cpf = cpf
        self.pessoas = int(pessoas)
        self.tipo_quarto = tipo_quarto
        self.dias = int(dias)
        self.valor = int(valor)
        self.status = status.strip()

    def to_csv(self):
        return f"{self.id},{self.titular},{self.cpf},{self.pessoas},{self.tipo_quarto},{self.dias},{self.valor},{self.status}\n"

    @classmethod
    def from_csv(cls, linha):
        partes = linha.strip().split(",")
        return cls(*partes)
