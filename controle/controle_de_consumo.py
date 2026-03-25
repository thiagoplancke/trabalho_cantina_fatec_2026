from controle.controle_de_estoque import Produto, Estoque
from controle.controle_de_pagamento import Pagamento
from rich import print

from estrutura.estruturas import Lista



class Venda:
    def __init__(self,produto,nome_comprador,categoria,curso, quantidade_vendida,data_hora, n,valor_total = 0):
        self.produto = produto
        self.nome_comprador = nome_comprador
        self.quantidade_vendida = quantidade_vendida
        self.valor_total = valor_total
        self.categoria = categoria
        self.curso = curso
        self.data_hora = data_hora
        self.nome_produto = n


    def vender(self):
        if self.produto is None:
            print("\n[bold red]❌ Produto não existe![/bold red]")
            return

        if self.produto.tamanho() == 0:
            print("\n[bold red]❌ Estoque vazio![/bold red]")
            return

        if self.quantidade_vendida > self.produto.tamanho():
            print(f"\n[bold yellow]⚠️ Estoque insuficiente! Disponível: {self.produto.tamanho()}[/bold yellow]")
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
            self.data_hora,
            self.nome_produto
        )

        return pagamento