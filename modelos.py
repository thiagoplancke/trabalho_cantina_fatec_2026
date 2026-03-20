class Produto():
    def __init__(self,nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome

        self.preco_compra = preco_compra

        self.preco_venda = preco_venda

        self.data_compra = data_compra

        self.data_vencimento = data_vencimento

        self.quantidade =quantidade

    def __str__(self):
        return (f"PRODUTO: {self.nome:15} | Estoque: {self.quantidade:3} | "
            f"Venda: R${self.preco_venda:.2f} | Vence: {self.data_vencimento}")
    



class Pagamento():
    def __init__(self,nome_pagador, categoria, curso, valor, data_hora):
        self.nome_pagador = nome_pagador
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data_hora = data_hora