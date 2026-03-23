from controle_de_estoque import Produto, Estoque
from controle_de_consumo import Venda
from estruturas import Lista
from rich.table import Table
from rich import print
from rich.panel import Panel



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


print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


inicio = Panel(title="CANTINA FATEC",renderable="Bem vindo(a) a CANTINA FATEC!\n\nPressione ENTER para entrar!",width=40)
print(inicio)
print("\n")
print("\n")
entrar = input()
print("\n")

while True:
    menu = Table(title="Menu", show_lines=True)

    menu.add_column("Produtos",justify="center")
    menu.add_column("Preço",justify="center")
    menu.add_column("Data de Abastecimento",justify="center")
    menu.add_column("Data de Validade",justify="center")
    menu.add_column("Quantidade", justify="center")


    for i in estoque_produtos.ver_items_estoque():
        menu.add_row(i[1].nome,f"R$ {i[1].preco:.2f}",i[1].data_compra,i[1].validade,str(i[1].quantidade))
    
    print(menu)
    

    
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

        historico = Table(title="Histórico de Vendas", show_lines=True)

        historico.add_column("Nome",justify="left")
        historico.add_column("Categoria",justify="center")
        historico.add_column("Curso",justify="center")
        historico.add_column("valor Gasto",justify="center")
        historico.add_column("Data e Hora", justify="center")


        for item in historico_pagamento.percorrer():
            historico.add_row(item.nome,item.categoria,item.curso,f"R$ {item.valor:.2f}",item.data_hora)
        print(historico)
            
    if opcao == "0":
        break
