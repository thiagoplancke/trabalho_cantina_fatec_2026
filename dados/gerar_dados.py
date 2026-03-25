from faker import Faker
from controle.controle_de_pagamento import Pagamento
from estrutura.estruturas import Lista
import random

fake = Faker("pt_BR")


PRODUTOS = [
    {"nome": "coxinha", "preco": 6},
    {"nome": "pastel", "preco": 7},
    {"nome": "coca cola", "preco": 5},
    {"nome": "suco", "preco": 4},
]


def gerar_dados_fake(quantidade=20):
    historico = Lista()

    for _ in range(quantidade):
        nome_cliente = fake.name()
        categoria = random.choice(["Aluno", "Professor"])
        curso = random.choice(["IA", "ESG"])

        produto = random.choice(PRODUTOS)
        quantidade_comprada = random.randint(1, 3)

        valor_total = produto["preco"] * quantidade_comprada

        data_hora = fake.date_time_this_year().strftime("%d/%m/%Y %H:%M")

        pagamento = Pagamento(
            nome_cliente,
            categoria,
            curso,
            valor_total,
            data_hora,
            produto["nome"]
        )

        historico.adicionar(pagamento)

    return historico