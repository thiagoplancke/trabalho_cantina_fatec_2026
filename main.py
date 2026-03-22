from controle_de_estoque import Produto, Estoque
from controle_de_consumo import Venda
from estruturas import Lista

historico_pagamento = Lista()

estoque_produtos = Estoque()


coxinha = Produto("cOxinhA",6,"13/05/22","15/03/22",5)
coca_cola = Produto("coca cola",5,"12/03/22","15/03/22",7)


estoque_produtos.adicionar_produto(coxinha)

estoque_produtos.adicionar_produto(coca_cola)




while True:
    print("Estoque: ")

    estoque_produtos.ver_items_estoque()

    
    print("\n\n1 - Comprar\n2 - Historico de Compras\n0 - Sair")
    
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o seu nome: ")
        curso = input("Digite o seu curso(IA/ESG): ")
        categoria = input("Digite a sua categoria(Aluno/Professor) ")
        produto = input("Digite o nome do produto que deseja comprar: ")
        quantidade = int(input("Digite a quantidade do produto que deseja comprar: "))

        venda = Venda(estoque_produtos.pegar_produto_estoque(produto),nome,categoria,curso,quantidade,"14/03/22")

        
        resultado = venda.vender()
        if resultado == None:
            print("Escolha outro produto")

        else:    

            historico_pagamento.adicionar(resultado)



    if opcao == "2":

        print(historico_pagamento.percorrer())

    if opcao == "0":
        break
