from controle_de_estoque import Produto, Estoque
from controle_de_consumo import Venda
from estruturas import Lista

historico_pagamento = Lista()
coxinha = Produto("cOxinhA",6,"13/05/22","15/03/22",5)
coca_cola = Produto("coca cola",5,"12/03/22","15/03/22",7)


estoque_produtos = Estoque()
estoque_produtos.adicionar_produto(coxinha)
estoque_produtos.adicionar_produto(coca_cola)

venda1 = Venda(estoque_produtos.pegar_produto_estoque("Coxinha"),"Thiago","Aluno","IA",1,"21/03/25")
historico_pagamento.adicionar(venda1.vender())
venda1 = Venda(estoque_produtos.pegar_produto_estoque("CoCA Cola"),"Thiago","Aluno","IA",1,"21/03/25")
historico_pagamento.adicionar(venda1.vender())
print(historico_pagamento.percorrer())


print(estoque_produtos.ver_items_estoque())

