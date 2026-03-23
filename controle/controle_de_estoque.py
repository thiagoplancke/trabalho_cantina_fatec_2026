from estrutura.estruturas import Dicionario
from estrutura.estruturas import Lista
from datetime import *

class Produto:
    def __init__(self, nome, preco,data_compra,validade):
        self.nome = nome.lower()
        self.preco = preco
        self.data_compra = datetime.strptime(data_compra, "%d/%m/%y")
        self.validade = datetime.strptime(validade, "%d/%m/%y")

    

class Estoque:
    def __init__(self):
        self.estoque = Dicionario()
    


    def adicionar_produto(self, produto):
        lista_produto = self.estoque.buscar(produto.nome)

        if lista_produto is None:
            lista_produto = Lista()
            lista_produto.adicionar(produto)
            self.estoque.adicionar(produto.nome, lista_produto)
        else:
            inserido = False

            for i in range(lista_produto.tamanho()):
                atual = lista_produto.acessar(i)

                if produto.validade < atual.validade:
                    lista_produto.inserir(i, produto)
                    inserido = True
                    break

            if not inserido:
                lista_produto.adicionar(produto)
    
    def pegar_produto_estoque(self,produto_nome):

        return self.estoque.buscar(produto_nome.lower())
    
    def ver_items_estoque(self):
        return self.estoque.ver_items()
