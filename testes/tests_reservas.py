import unittest
from unittest.mock import patch, MagicMock
from models.reserva import Reserva
import services.cadastro as cadastro
import services.alterar as alteracao
import services.checkin as checkin
import services.checkout as checkout
import services.relatorio as relatorio


class TestSistemaReservas(unittest.TestCase):

    def setUp(self):
        self.reserva_r = Reserva(1, "JOÃO", "12345678900", 2, "S", 3, 600, "R")
        self.reserva_a = Reserva(2, "JOÃO", "12345678900", 2, "S", 3, 600, "A")
        self.reserva_f = Reserva(3, "JOÃO", "12345678900", 2, "S", 3, 600, "F")

    @patch('services.cadastro.salvar_reservas')
    @patch('services.cadastro.carregar_reservas', return_value=[])
    @patch('builtins.input', side_effect=['João', '12345678900', '2', 'S', '3'])
    @patch('utils.validacoes.validar_nome', return_value=True)
    @patch('utils.validacoes.validar_cpf', return_value=True)
    @patch('utils.validacoes.validar_numero', return_value=True)
    @patch('utils.calculos.calcular_valor', return_value=600)
    def test_cadastro_reserva(self, calc, vnum, vcpf, vnome, input_mock, carregar, salvar):
        cadastro.executar_cadastro()
        salvar.assert_called_once()

    @patch('services.alterar.salvar_reservas')
    @patch('services.alterar.carregar_reservas')
    @patch('builtins.input', side_effect=["12345678900", "1", "1", "3"])
    @patch('utils.validacoes.validar_cpf', return_value=True)
    @patch('utils.validacoes.validar_numero', return_value=True)
    @patch('utils.calculos.calcular_valor', return_value=900)
    def test_alteracao_numero_pessoas(self, calc, vnum, vcpf, input_mock, carregar, salvar):
        reserva = self.reserva_r
        carregar.return_value = [reserva]
        alteracao.executar_alteracao()
        self.assertEqual(reserva.pessoas, 3)
        self.assertEqual(reserva.valor, 900)

    @patch('services.checkin.salvar_reservas')
    @patch('services.checkin.carregar_reservas')
    @patch('builtins.input', side_effect=["12345678900", "1"])
    @patch('utils.validacoes.validar_cpf', return_value=True)
    def test_checkin(self, vcpf, input_mock, carregar, salvar):
        reserva = self.reserva_r
        carregar.return_value = [reserva]
        checkin.executar_checkin()
        self.assertEqual(reserva.status, "A")

    @patch('services.checkout.salvar_reservas')
    @patch('services.checkout.carregar_reservas')
    @patch('builtins.input', side_effect=["12345678900", "2"])
    @patch('utils.validacoes.validar_cpf', return_value=True)
    def test_checkout(self, vcpf, input_mock, carregar, salvar):
        reserva = self.reserva_a
        carregar.return_value = [reserva]
        checkout.executar_checkout()
        self.assertEqual(reserva.status, "F")

    @patch('services.relatorio.carregar_reservas')
    def test_relatorio_status(self, carregar):
        carregar.return_value = [self.reserva_r, self.reserva_a]
        with patch('builtins.print') as mocked_print:
            relatorio.filtrar_por_status("R")
            chamadas = [c.args[0] for c in mocked_print.call_args_list if c.args]
            self.assertTrue(any(">>> Total: 1 reserva(s)." in c for c in chamadas))

    @patch('services.relatorio.carregar_reservas')
    def test_relatorio_valor_finalizado(self, carregar):
        carregar.return_value = [self.reserva_r, self.reserva_f]
        with patch('builtins.print') as mocked_print:
            relatorio.relatorio_valor_total_finalizado()
            chamadas = [c.args[0] for c in mocked_print.call_args_list if c.args]
            self.assertTrue(any("Valor total recebido por reservas finalizadas" in c for c in chamadas))

    @patch('services.relatorio.carregar_reservas')
    @patch('builtins.input', return_value="12345678900")
    @patch('utils.validacoes.validar_cpf', return_value=True)
    def test_relatorio_por_cpf(self, vcpf, input_mock, carregar):
        carregar.return_value = [self.reserva_r, self.reserva_a]
        with patch('builtins.print') as mocked_print:
            relatorio.relatorio_por_cpf()
            chamadas = [c.args[0] for c in mocked_print.call_args_list if c.args]
            self.assertTrue(any(">>> Total: 2 reserva(s)." in c for c in chamadas))


if __name__ == '__main__':
    unittest.main()
