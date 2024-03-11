import json
import re
import ply.lex as lex

tokens = ['LISTAR', 'SAIR', 'SALDO', 'MOEDA', 'SELECIONAR']

t_ignore = ' \t\n'

def t_MOEDA(t):
    r'((1|2)e|(1|2|5|10|20|50)c)'
    if t.value[-1] == 'e':
        t.lexer.saldo += int(t.value[:-1])
    else:
        t.lexer.saldo += int(t.value[:-1]) / 100
    return t

def t_LISTAR(t):
    r'LISTAR'
    print("Lista de produtos disponíveis:")
    for produto, detalhes in t.lexer.data.items():
        print(f"ID: {detalhes['id']}, Nome: {produto}, Preço: {detalhes['preco']}€")
    return t

def t_SALDO(t):
    r'SALDO'
    print(f"Saldo disponível: {t.lexer.saldo}€")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s\d+'
    produto_id = int(t.value.split()[1])
    produto = next((detalhes for detalhes in t.lexer.data.values() if detalhes["id"] == produto_id), None)
    if produto:
        if t.lexer.saldo >= produto['preco']:
            t.lexer.saldo -= produto['preco']
            print(f"Compra efetuada com sucesso: Produto {produto_id}")
        else:
            print(f"Saldo insuficiente para comprar: Produto {produto_id}")
    else:
        print(f"Produto inexistente com ID: {produto_id}")
    return t

def t_SAIR(t):
    r'SAIR'
    print(f"Troco: {t.lexer.saldo}€")
    t.lexer.flag = True
    return t

def t_error(t):
    print("Comando inválido.")
    t.lexer.skip(1)

def main():
    lexer = lex.lex()
    
    with open("./TPC5/artigos.json", "r") as file:
        data = json.load(file)

    lexer.data = data
    lexer.flag = False
    lexer.saldo = 0

    # Display initial message
    print("Bem-vindo à máquina de venda automática.\n")
    print("Comandos disponíveis:\n")
    print("-> LISTAR\n")
    print("-> SALDO\n")
    print("-> MOEDA\n")
    print("-> SELECIONAR\n")
    print("-> SAIR\n")


    # Main loop
    while not lexer.flag:
        input_user = input("Operação a realizar: ")
        lexer.input(input_user)
        token = lexer.token()
        if not token:
            print("Comando inválido.")

if __name__ == "__main__":
    main()