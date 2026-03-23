# 🛒 Cantina Fatec — Sistema de Controle de Estoque com Prioridade por Validade

## 📌 Descrição do Projeto

Este projeto simula o funcionamento de uma cantina universitária, permitindo o controle de:

* 📦 Estoque de produtos perecíveis
* 💳 Registro de pagamentos
* 🛒 Consumo dos clientes

O sistema prioriza automaticamente a venda de produtos com **menor data de validade**, seguindo a estratégia **FEFO (First Expire, First Out)**.

---

## 🎯 Objetivo Acadêmico

Desenvolvido para as disciplinas:

* Estrutura de Dados
* Linguagem de Programação

Com foco em:

* Implementação de estruturas de dados próprias
* Aplicação prática em um problema real
* Organização modular do código

---

## 🧠 Estruturas de Dados Utilizadas

As estruturas foram implementadas manualmente:

* **Lista** → utilizada para armazenar produtos ordenados por validade
* **Dicionário (Hash Map)** → utilizado para mapear produtos por nome

---

## ⚙️ Lógica Principal (FEFO)

Produtos com o mesmo nome são armazenados em uma lista ordenada por validade:

Exemplo:

Coxinha:

* vence dia 05
* vence dia 10
* vence dia 20

Ao vender:
→ sempre remove o primeiro da lista (produto mais próximo de vencer)

---

## 🔄 Fluxo do Sistema

1. Produto é adicionado ao estoque
2. O sistema insere o produto na posição correta (ordenado por validade)
3. Cliente realiza uma compra
4. O sistema remove o produto mais próximo de vencer
5. O pagamento é registrado

---

## 📊 Funcionalidades

* Cadastro de produtos
* Controle de estoque com prioridade por validade
* Registro de vendas
* Histórico de pagamentos

---

## 🧪 Dados e Persistência

* Dados podem ser gerados automaticamente
* Persistência usando `pickle`

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/thiagoplancke/trabalho_cantina_fatec_2026.git
cd SEU-REPOSITORIO
```

### 2. Criar ambiente virtual (opcional)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o sistema

```bash
python main.py
```

---

## 🧠 Conceito Importante

O sistema utiliza o conceito:

**FEFO (First Expire, First Out)**

Isso garante que produtos com menor validade sejam vendidos primeiro, evitando desperdício.

---

## 👨‍💻 Autor

Thiago Plancke
Fatec Rio Claro

---

## 📅 Prazo

Entrega: 26 Março de 2026
