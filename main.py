from services.cadastro import executar_cadastro
from services.checkin import executar_checkin
from services.checkout import executar_checkout
from services.alterar import executar_alteracao
from services.relatorio import executar_relatorio

def exibir_menu_principal():
    return """
    ------ MENU PRINCIPAL ------
    1 - Cadastrar uma reserva
    2 - Realizar check-in
    3 - Realizar check-out
    4 - Alterar reserva
    5 - Relatórios
    6 - Sair
    """

def main():
    while True:
        print(exibir_menu_principal())
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                executar_cadastro()
            case "2":
                executar_checkin()
            case "3":
                executar_checkout()
            case "4":
                executar_alteracao()
            case "5":
                executar_relatorio()
            case "6":
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
