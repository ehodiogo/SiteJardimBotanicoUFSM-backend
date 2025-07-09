from django.test import TestCase
from datetime import date, time
from agendamento.models import Agendamento
from bolsista.models import Bolsista, HorarioBolsista


class BuscarBolsistasDisponiveisTest(TestCase):
    def setUp(self):
        self.bolsista1 = Bolsista.objects.create(
            nome="João",
            email="joao@example.com",
            matricula="12345",
            curso="Biologia",
            periodo="5º",
        )

        self.bolsista2 = Bolsista.objects.create(
            nome="Maria",
            email="maria@example.com",
            matricula="67890",
            curso="Ecologia",
            periodo="3º",
        )

        # João: disponível na quarta (weekday=2) das 9h às 11h
        HorarioBolsista.objects.create(
            bolsista=self.bolsista1,
            dia_semana=2,
            horario_inicio=time(9, 0),
            horario_fim=time(11, 0),
        )

        # Maria: disponível na quarta (weekday=2) das 14h às 16h
        HorarioBolsista.objects.create(
            bolsista=self.bolsista2,
            dia_semana=2,
            horario_inicio=time(14, 0),
            horario_fim=time(16, 0),
        )

        # Maria: disponível na quinta (weekday=3) das 10h às 12h
        HorarioBolsista.objects.create(
            bolsista=self.bolsista2,
            dia_semana=3,
            horario_inicio=time(10, 0),
            horario_fim=time(12, 0),
        )

    def test_busca_bolsista_disponivel_no_horario(self):
        # Quarta-feira, 25/06/2025 às 9h30 → João disponível
        agendamento = Agendamento(
            data_agendamento=date(2025, 6, 25), horario_pretendido=time(9, 30)
        )
        bolsistas = agendamento.buscar_bolsista()

        print("Bolsistas disponíveis:", list(bolsistas))

        self.assertIn(self.bolsista1, bolsistas)
        self.assertNotIn(self.bolsista2, bolsistas)

    def test_sem_bolsistas_disponiveis(self):
        # Sexta-feira, 27/06/2025 → ninguém cadastrado
        agendamento = Agendamento(
            data_agendamento=date(2025, 6, 27),  # sexta
            horario_pretendido=time(10, 0),
        )
        bolsistas = agendamento.buscar_bolsista()

        print("Bolsistas disponíveis:", list(bolsistas))

        self.assertEqual(bolsistas.count(), 0)

    def test_bolsista_no_horario_exato_inicio(self):
        # Quinta-feira, 26/06/2025 → Maria começa às 10:00
        agendamento = Agendamento(
            data_agendamento=date(2025, 6, 26), horario_pretendido=time(10, 0)
        )
        bolsistas = agendamento.buscar_bolsista()

        print("Bolsistas disponíveis:", list(bolsistas))

        self.assertIn(self.bolsista2, bolsistas)
        self.assertNotIn(self.bolsista1, bolsistas)
