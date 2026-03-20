from controle_de_estoque import Produto, Estoque



class Venda:
    def __init__(self,produto,nome_comprador, quantidade_vendida, valor_total = 0):
        self.produto = produto
        self.nome_comprador = nome_comprador
        self.quantidade_vendida = quantidade_vendida
        self.valor_total = valor_total


    def vender(self):
        if self.produto == None:
            return "Produto não existe"
        if self.quantidade_vendida > self.produto.quantidade:
            return f"Estoque insuficiente"
        self.produto.quantidade -= self.quantidade_vendida
        self.valor_total = self.produto.preco * self.quantidade_vendida

        return f"{self.nome_comprador} comprou {self.quantidade_vendida} {self.produto.nome} no valor total R${self.valor_total}"


coxinha = Produto("cOxinhA",6,"13/05/22","15/03/22",5)


estoque_produtos = Estoque()
estoque_produtos.adicionar_produto(coxinha)

venda1 = Venda(estoque_produtos.pegar_produto_estoque("Coinha"),"Thiago", 3)

print(venda1.vender())



