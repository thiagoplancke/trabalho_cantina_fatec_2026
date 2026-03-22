from controle_de_estoque import Produto, Estoque
from controle_de_pagamento import Pagamento

from estruturas import Lista



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
        if self.produto == None:
            return "Produto não existe"
        if self.quantidade_vendida > self.produto.quantidade:
            return f"Estoque insuficiente"
        self.produto.quantidade -= self.quantidade_vendida
        self.valor_total = self.produto.preco * self.quantidade_vendida
        pagamento = Pagamento(self.nome_comprador,self.categoria,self.curso,self.valor_total,self.data_hora)
        return pagamento




