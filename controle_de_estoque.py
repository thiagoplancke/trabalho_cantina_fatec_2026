from estruturas import Dicionario


class Produto:
    def __init__(self, nome, preco,data_compra,validade,quantidade):
        self.nome = nome.lower()
        self.preco = preco
        self.data_compra = data_compra
        self.quantidade = quantidade
        self.validade = validade

    def __repr__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Abastecido: {self.data_compra} | Validade: {self.validade} | Quantidade: {self.quantidade} unidades"


class Estoque:
    def __init__(self):
        self.estoque = Dicionario()
    


    def adicionar_produto(self,produto):
        self.estoque.adicionar(produto.nome,produto)
    
    def pegar_produto_estoque(self,produto_nome):

        return self.estoque.buscar(produto_nome.lower())
    
    def ver_items_estoque(self):
        return self.estoque.ver_items()
