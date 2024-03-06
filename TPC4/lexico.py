import ply.lex as lex

tokens = (
    'COMMAND',
    'FROM',
    'WHERE',
    'VARS_TABS',
    'VALORES',
    'SIMBOLOS',
    'SEPARADORES'
)

t_COMMAND = r'[Ss][Ee][Ll][Ee][Cc][Tt]|[Uu][Pp][Dd][Aa][Tt][Ee]|[Dd][Ee][Ll][Ee][Tt][Ee]'
t_FROM = r'[Ww][Hh][Ee][Rr][Ee]'
t_WHERE = r'[Ff][Rr][Oo][Mm]'
t_VARS_TABS = r'[A-Za-z]\w*'
t_VALORES = r'-?\d+'
t_SEPARADORES = r",|;"
t_SIMBOLOS = r'>=|<=|<|>|==|='

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = "SELECT id, nome, salario FROM empregados WHERE salario >= 820"

lexer.input(data)

# Tokenize
for token in lexer:
    print(token)