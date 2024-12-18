import ply.lex as lex
import json

# Define tokens
tokens = (
    'sbracket',      # [
    'sbracketF',     # ]
    'curlyb',        # {
    'curlybF',       # }
    'key_id',        # "id"
    'key_name',      # "name"
    'key_course',    # "course"
    'key_grades',    # "grades"
    'key_average',   # "average"
    'string_value',  # String values
    'number_value',  # Numbers
    'comma',         # ,
    'colon',         # :
)

# Token patterns
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
    r'"[^"]*"'
    return t

def t_number_value(t):
    r'[0-9]+(\.[0-9]+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Symbols
t_sbracket = r'\['
t_sbracketF = r'\]'
t_curlyb = r'\{'
t_curlybF = r'\}'
t_colon = r':'
t_comma = r','

# Ignored characters
t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Main section for testing
if __name__ == "__main__":
    with open('input.json', 'r') as json_file:
      json_string = json_file.read()
    print("\n\n------ Complete Structure ------\n\n\n" + json_string + "\n\n------Validation ------\n")

    input_str = ' '
    while input_str != '':
        input_str = json_string

        if input_str != '':
            lexer.input(input_str)

            for tok in lexer:
                print(tok)
        break
