import ply.lex as lex

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
    'number_value', # Números enteros
    'comma',        # ,
    'colon',        # :
)

# Definición de patrones para los tokens clave
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

# Token para cadenas de texto (valores de strings)
def t_string_value(t):
    r'"[^"]*"'  # Captura cualquier texto dentro de comillas dobles
    return t

# Token para valores numéricos
def t_number_value(t):
    r'[0-9]+(\.[0-9]+)?'  # Reconoce enteros y decimales
    t.value = float(t.value) if '.' in t.value else int(t.value)  # Convierte a int o float
    return t


# Tokens para símbolos especiales
t_sbracket = r'\['
t_sbracketF = r'\]'
t_curlyb = r'\{'
t_curlybF = r'\}'
t_colon = r':'
t_comma = r','

# Ignorar espacios y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

if __name__ == '__main__':
    # Leer el archivo JSON
    try:
        with open('input.json', 'r', encoding='utf-8') as json_file:
            json_string = json_file.read()
    except FileNotFoundError:
        print("El archivo 'input.json' no se encontró. Asegúrate de que esté en el mismo directorio que este script.")
        exit()

    print("\n\n------ Complete Structure ------\n\n\n" + json_string + "\n\n------ Validation ------\n")

    input_str = json_string  # Entrada para el lexer

    # Validar e imprimir los tokens generados
    if input_str:
        lexer.input(input_str)
        for tok in lexer:
            print(tok)