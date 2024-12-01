import ply.lex as lex
import json

# Definición de tokens
tokens = (
    'sbracket',     # [
    'sbracketF',    # ]
    'curlyb',       # {
    'curlybF',      # }
    'key_id',       # "id"
    'key_name',     # "name"
    'key_course',   # "course"
    'key_grades',   # "grades"
    'key_average',  # "average"
    'string_value', # "cadena de texto"
    'number_value', # 0-9
    'comma',        # ,
    'colon',        # :
    'lbracket',     # [
    'rbracket'      # ]
)

# Definición de patrones para los tokens
def t_key_id(t):
    r'"id"'
    return t

def t_key_name(t):
    r'"name"'
    return t

def t_key_course(t):
    r'"course"'
    return t

def t_key_grades(t):
    r'"grades"'
    return t

def t_key_average(t):
    r'"average"'
    return t

def t_string_value(t):
    r'"[@\.A-Za-z0-9 \(\)\'_\-]+"'
    return t

def t_number_value(t):
    r'[0-9]+'
    return t

# Símbolos especiales
t_sbracket = r'\['
t_sbracketF = r'\]'
t_curlyb = r'\{'
t_curlybF = r'\}'
t_colon = r':'
t_comma = r'\,'
t_lbracket = r'\['
t_rbracket = r'\]'

# Ignorar espacios y tabulaciones
t_ignore = '\t|\n| '

# Manejo de errores
def t_error(t):
    print('Illegal character', t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

if __name__ == '__main__':
    # Leer el archivo JSON
    with open('input.json', 'r') as json_file:
        json_string = json_file.read()

    print("\n\n------ Complete Structure ------\n\n\n" + json_string + "\n\n------Validation ------\n")

    input_str = json_string  # Entrada del lexer

    if input_str:
        lexer.input(input_str)

        # Imprimir los tokens generados
        for tok in lexer:
            print(tok)
