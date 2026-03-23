from controle.controle_de_estoque import Produto, Estoque
from controle.controle_de_pagamento import Pagamento

from estrutura.estruturas import Lista



class Venda:
    def __init__(self,produto,nome_comprador,categoria,curso, quantidade_vendida,data_hora, valor_total = 0):
        self.produto = produto
        self.nome_comprador = nome_comprador
        self.quantidade_vendida = quantidade_vendida
        self.valor_total = valor_total
        self.categoria = categoria
        self.curso = curso
        self.data_hora = data_hora


    def vender(self):
        if self.produto is None:
            print("Produto não existe")
            return

        if self.produto.tamanho() == 0:
            print("Estoque vazio")
            return

        if self.quantidade_vendida > self.produto.tamanho():
            print("Estoque insuficiente")
            return

        valor_total = 0

        for _ in range(self.quantidade_vendida):
            item_removido = self.produto.remover(0)
            valor_total += item_removido.preco

        self.valor_total = valor_total

        pagamento = Pagamento(
            self.nome_comprador,
            self.categoria,
            self.curso,
            self.valor_total,
            self.data_hora
        )

        return pagamento