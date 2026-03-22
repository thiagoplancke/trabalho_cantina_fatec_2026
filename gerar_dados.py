from faker import Faker
from controle_de_pagamento import Pagamento
from estruturas import Lista
import random

fake = Faker("pt_BR")


def gerar_dados_fake(quantidade=20):
    historico = Lista()

    for _ in range(quantidade):
        nome = fake.name()
        categoria = random.choice(["Aluno", "Professor", "Servidor"])
        curso = random.choice(["IA", "ESG"])
        valor = round(random.uniform(5, 30), 2)
        data_hora = fake.date_time_this_year().strftime("%d/%m/%Y %H:%M")

        pagamento = Pagamento(nome, categoria, curso, valor, data_hora)
        historico.adicionar(pagamento)

    return historico