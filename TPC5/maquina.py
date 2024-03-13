import json
import re
import ply.lex as lex

tokens = ['LISTAR', 'SAIR', 'SALDO', 'MOEDA', 'SELECIONAR', 'ADICIONAR']

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
    print("Lista de produtos:")
    print("""ID | NOME | QUANTIDADE | PREÇO""")
    for produto, detalhes in t.lexer.data.items():
        print(f" {detalhes['id']} | {produto} | {detalhes['quantidade']} | {detalhes['preco']}€")
    return t

def t_ADICIONAR(t):
    r'ADICIONAR\s+\w+\s+\d+\s+\d+(\.\d+)?'  # Exemplo: ADICIONAR produto 7 1.50
    input_parts = t.value.split()
    produto_nome = input_parts[1]
    quantidade = int(input_parts[2])
    preco = float(input_parts[3])
    
    if produto_nome in t.lexer.data:
        t.lexer.data[produto_nome]['quantidade'] += quantidade
        t.lexer.data[produto_nome]['preco'] = preco
    else:
        novo_produto = {
            'id': len(t.lexer.data) + 1,
            'preco': preco,
            'quantidade': quantidade
        }
        t.lexer.data[produto_nome] = novo_produto
    print(f"{quantidade} unidades de {produto_nome} adicionadas ao estoque.")
    
        # Salvar os dados atualizados no arquivo JSON
    with open("./TPC5/artigos.json", "w") as file:
        json.dump(t.lexer.data, file, indent=4)
    return t

def t_SALDO(t):
    r'SALDO'
    print(f"Saldo disponível: {t.lexer.saldo}€")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s\d+'
    produto_id = int(t.value.split()[1])
    produto = next((detalhes for detalhes in t.lexer.data.values() if detalhes["id"] == produto_id), None)
    for nome, detalhes in t.lexer.data.items():
        if detalhes["id"] == produto_id:
            nome_produto = nome
    if produto:
        if t.lexer.saldo >= produto['preco']:
            if produto['quantidade'] > 0:
                t.lexer.saldo -= produto['preco']
                produto['quantidade'] -= 1
                print(f"Compra efetuada com sucesso: {nome_produto}")
            else:
                print(f"Produto {produto_id} esgotado.")
        else:
            print(f"Saldo insuficiente para comprar: {nome_produto}")
    else:
        print(f"Produto inexistente com código: {produto_id}")
        
        # Salvar os dados atualizados no arquivo JSON
    with open("./TPC5/artigos.json", "w") as file:
        json.dump(t.lexer.data, file, indent=4)
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
    print("Bem-vindo à máquina de venda automática.")
    print("Comandos disponíveis:")
    print("-> LISTAR")
    print("-> SALDO")
    print("-> MOEDA")
    print("-> SELECIONAR")
    print("-> ADICIONAR")
    print("-> SAIR")

    # Main loop
    while not lexer.flag:
        input_user = input("Operação a realizar: ")
        lexer.input(input_user)
        token = lexer.token()
        if not token:
            print("Comando inválido.")

if __name__ == "__main__":
    main()