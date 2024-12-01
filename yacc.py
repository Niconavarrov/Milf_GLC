import ply.yacc as yacc
from lexer import tokens  # Importamos los tokens del lexer
import json

# Reglas gramaticales
def p_start(p):
    '''S : sbracket A sbracketF'''
    print("Validating: Start of JSON array")
    p[0] = p[2]

def p_multiple_records(p):
    '''A : curlyb B curlybF comma A'''
    print("Validating: Multiple records")
    p[0] = [p[2]] + p[5]

def p_single_record(p):
    '''A : curlyb B curlybF'''
    print("Validating: Single record")
    p[0] = [p[2]]

def p_record_structure(p):
    '''B : key_id colon number_value comma C'''
    print(f"Validating: Record with ID {p[3]}")
    record = {"id": int(p[3])}
    record.update(p[5])
    p[0] = record

def p_name(p):
    '''C : key_name colon string_value comma D'''
    print(f"Validating: Name = {p[3]}")
    record = {"name": p[3].strip('"')}
    record.update(p[5])
    p[0] = record

def p_course(p):
    '''D : key_course colon string_value comma E'''
    print(f"Validating: Course = {p[3]}")
    record = {"course": p[3].strip('"')}
    record.update(p[5])
    p[0] = record

def p_grades(p):
    '''E : key_grades colon sbracket G sbracketF comma F'''
    print(f"Validating: Grades = {p[4]}")
    record = {"grades": p[4]}
    record.update(p[7])
    p[0] = record

def p_grade_list(p):
    '''G : number_value
         | number_value comma G'''
    if len(p) == 2:
        print(f"Validating: Single grade = {p[1]}")
        p[0] = [int(p[1])]
    else:
        print(f"Validating: Grade list = {p[1]}, {p[3]}")
        p[0] = [int(p[1])] + p[3]

def p_average(p):
    '''F : key_average colon number_value'''
    print(f"Validating: Average = {p[3]}")
    p[0] = {"average": float(p[3])}

def p_error(p):
    print("Syntax error at", p.value if p else "EOF")

# Construir el parser
parser = yacc.yacc()

#Abrir /input.json
with open('input.json', 'r') as json_file:
   json_string = json_file.read()

#Definir array de alamcenamiento de datos INDIVIDUAL y COLECTIVO
individual_data = []
data = []

# Validación del JSON
print("\n------ Rules Validation (Collected data) ------")
try:
    result = parser.parse(json_string)
    print("\n------ Complete Structure ------\n")
    print(json.dumps(result, indent=4))  # Imprime datos procesados en formato JSON
    data = result  # Guarda los datos procesados
except Exception as e:
    print(f"Error during parsing: {e}")

# Exportación a CSV
if len(data) > 0:
    with open("employees.csv", "w") as archivo:
        # Encabezados del CSV
        archivo.write("ID,Name,Course,Grades,Average\n")
        for record in data:
            archivo.write(
                f'{record["id"]},"{record["name"]}","{record["course"]}",'
                f'"{",".join(map(str, record["grades"]))}",{record["average"]}\n'
            )
    print("Data successfully exported to employees.csv")
