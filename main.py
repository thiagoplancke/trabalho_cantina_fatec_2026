from controle_de_estoque import Produto, Estoque
from controle_de_consumo import Venda
from estruturas import Lista



from salvar_dados import carregar_dados, salvar_dados
from gerar_dados import gerar_dados_fake

dados_fake = carregar_dados()

if dados_fake is None:
    dados_fake = gerar_dados_fake()
    salvar_dados(dados_fake)




historico_pagamento = dados_fake

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
        if resultado is not None:
            historico_pagamento.adicionar(resultado)
            salvar_dados(historico_pagamento)



    if opcao == "2":

        for item in historico_pagamento.percorrer():
            print(item)
            
    if opcao == "0":
        break
