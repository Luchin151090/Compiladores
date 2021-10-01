import ply.lex as lex
# List of token names. This is always required
tokens = ('numero','cadena','flotante','doble_precision','typeid','id','headx','finishx','whilx','yesx','elsx','forx','claxx','e_s','equal','ope_plus','ope_minus', 'ope_mul', 'ope_div','ope_menor','ope_menor_igual','ope_mayor_igual','ope_mayor','ope_igualdad','ope_diferente','par_a', 'par_c','key_a','key_c','dos_puntos')
# Regular expression rules for simple tokens
t_ope_plus = r'\+'
t_ope_minus = r'-'
t_ope_mul = r'\*'
t_ope_div = r'/'
t_par_a=  r'\('
t_par_c= r'\)'
t_key_a=r'\{'
t_key_c=r'\}'
t_dos_puntos=r':'
t_ope_menor=r'\<'
t_ope_mayor=r'\>'
t_ope_menor_igual=r'\<='
t_ope_mayor_igual=r'\>='
t_ope_diferente=r'\!='
t_ope_igualdad=r'\=='
t_typeid=r'int|float|str|double'
t_id=r'[a-z][a-zA-Z,0-9]*'
t_equal=r'='

def t_headx(t):
    r'headx'
    t.value=str(t.value)
    return t

def t_whilx(t):
    r'whilx'
    t.value=str(t.value)
    return t

def t_forx(t):
    r'forx'
    t.value=str(t.value)
    return t

def t_yesx(t):
    r'yesx'
    t.value=str(t.value)
    return t

def t_elsx(t):
    r'elsx'
    t.value=str(t.value)
    return t

def t_claxx(t):
    r'claxx'
    t.value=str(t.value)
    return t

def t_e_s(t):
    r'enterx|Printx'
    t.value=str(t.value)
    return t

def t_finishx(t):
    r'finishx'
    t.value=str(t.value)
    return t

def t_numero(t):
    r'\d+'
    t.value = int(t.value) # guardamos el valor del lexema
    return t
# A regular expression rule with some action code
def t_cadena(t):
    r'["][a-zA-Z,0-9, _]*["]'
    t.value = str(t.value)
    return t
def t_flotante(t):
    r'\d+'
    t.value = float(t.value) # guardamos el valor del lexema
    return t
def t_doble_precision(t):
    r'\d+'
    t.value = float(t.value) # guardamos el valor del lexema
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+|\s|\s+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'
# Error handling rule
def t_error(t):
    #print("Illegal character ' %s'" % t.value[0])
    t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()

f= open("bucle.txt","r")
# Test it out
data = f.read()
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok)
#print(tok.type, tok.value, tok.lineno, tok.lexpos)
