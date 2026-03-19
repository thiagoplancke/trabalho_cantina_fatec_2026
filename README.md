# 🛒 Cantina Fatec — Sistema de Controle com Estruturas de Dados

## 📌 Descrição do Projeto

Este projeto tem como objetivo simular o funcionamento de uma cantina universitária, permitindo o controle de:

* 📦 Estoque de produtos perecíveis
* 💳 Pagamentos realizados via PIX
* 🛒 Consumo dos clientes (integração entre estoque e pagamento)

O foco principal é a implementação de **estruturas de dados próprias**, sem uso direto de estruturas built-in do Python no domínio da aplicação.

---

## 🎯 Objetivo Acadêmico

O projeto foi desenvolvido para as disciplinas:

* Estrutura de Dados
* Linguagem de Programação 2

Com foco em:

* Implementação de estruturas como lista, fila, pilha e dicionário
* Aplicação prática dessas estruturas em um problema real
* Separação de responsabilidades e organização de código

---

## 🧠 Estruturas de Dados Utilizadas

As seguintes estruturas foram implementadas manualmente:

* **Lista** → base para armazenamento genérico
* **Fila (FIFO)** → controle de produtos perecíveis (prioridade para os mais antigos)
* **Pilha (LIFO)** → histórico de operações (opcional)
* **Dicionário (Hash Map)** → busca eficiente de produtos e clientes

---

## 🧩 Modelagem do Sistema

O sistema é dividido nas seguintes entidades principais:

* **Produto** → informações básicas do item
* **Lote** → controle de validade e quantidade (produtos perecíveis)
* **Estoque** → gerencia produtos e seus respectivos lotes
* **Pagamento** → registro de transações realizadas
* **Consumo** → relação entre cliente, produto e pagamento

---

## 🔄 Fluxo de Funcionamento

1. Um cliente seleciona um produto
2. O sistema verifica o estoque (priorizando os itens mais antigos)
3. O produto é removido do estoque
4. O pagamento é registrado
5. O consumo é armazenado para controle e auditoria

---

## 📊 Funcionalidades

* Cadastro e gerenciamento de produtos
* Controle de estoque com prioridade por validade
* Registro de pagamentos
* Controle de consumo por cliente
* Geração de relatórios de vendas e consumo

---

## 🧪 Geração e Persistência de Dados

* Utilização da biblioteca **Faker** para geração de dados aleatórios
* Persistência de dados utilizando **pickle**

---

## ⚙️ Regras do Projeto

* Não utilizar estruturas built-in diretamente na lógica do sistema
* Implementar estruturas próprias com encapsulamento
* Organização em classes com responsabilidades bem definidas

---

## 🚀 Estrutura do Projeto (planejada)

```
src/
 ├── estruturas/
 │    ├── lista.py
 │    ├── fila.py
 │    ├── pilha.py
 │    └── dicionario.py
 │
 ├── modelos/
 │    ├── produto.py
 │    ├── lote.py
 │    ├── pagamento.py
 │    └── consumo.py
 │
 ├── sistema/
 │    └── cantina.py
 │
 └── main.py
```

## 👨‍💻 Autor

Projeto desenvolvido por Thiago Plancke estudante da Fatec Rio Claro como parte da avaliação acadêmica.

---

## 📅 Prazo

Entrega final: 26 Março de 2026
