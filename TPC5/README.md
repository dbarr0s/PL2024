# TPC5 - Máquina Vending de Artigos
Pretende-se criar uma script de Python, que **analise e efetue pedidos**, para que sejam efetuadas **transações entre um cliente e uma máquina de vending.** 

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Resumo:
O programa desenvolvido neste **TPC5** deve responder às seguintes instruções:
- **LISTAR**: o cliente insere esta intrução e a script lista todos os **artigos da máquina e as suas informações**.
- **MOEDA**: o cliente começa por inserir a quantia que pretende no seguinte formato, **(1e, 2e, 1c, 2c, 5c, 10c, 20c, 50c)**. A máquina, consoante o valor inserido, vai adicionando o **valor ao saldo total do cliente**.
- **SALDO**: o cliente ao introduzir esta instrução, o programa devolve o **saldo** que o cliente tem naquele **preciso momento**.
- **SELECIONAR**: o cliente introduz a **instrução e o ID do artigo**, que pretende comprar, e verifica se o cliente tem **saldo suficiente** para efetuar a compra. Se tiver, **retira o valor ao saldo**, se não tiver, **não finaliza a transação.**
- **SAIR**: o programa **divulga/"devolve"** o troco ao cliente e finaliza o programa alterando o valor da **flag**.
