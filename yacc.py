import ply.yacc as yacc
from lexer import tokens  # Importamos los tokens del lexer
import json

# Variables para almacenar datos procesados
data = []

# Reglas gramaticales
def p_start(p):
    'S : sbracket A sbracketF'
    # Procesa la lista de alumnos
    p[0] = p[2]
    print("Parsed Data:", p[0])

def p_multiple_records(p):
    'A : curlyb B curlybF comma A'
    # Procesa un registro seguido de más registros
    p[0] = [p[2]] + p[4]

def p_single_record(p):
    'A : curlyb B curlybF'
    # Procesa un único registro
    p[0] = [p[2]]

def p_record_structure(p):
    'B : key_id colon number_value comma C'
    # Procesa el ID y delega al siguiente campo
    alumno = {"id": int(p[3])}
    alumno.update(p[5])  # Agrega los datos procesados en la regla C
    p[0] = alumno

def p_name(p):
    'C : key_name colon string_value comma D'
    # Procesa el nombre y delega al siguiente campo
    alumno = {"name": p[3].strip('"')}
    alumno.update(p[5])
    p[0] = alumno

def p_course(p):
    'D : key_course colon string_value comma E'
    # Procesa el curso y delega al siguiente campo
    alumno = {"course": p[3].strip('"')}
    alumno.update(p[5])
    p[0] = alumno

def p_grades(p):
    'E : key_grades colon lbracket G rbracket comma F'
    # Procesa las calificaciones y delega al siguiente campo
    alumno = {"grades": p[4]}  # p[4] contiene la lista de calificaciones
    alumno.update(p[7])
    p[0] = alumno

def p_grade_list(p):
    '''G : number_value
         | number_value comma G'''
    # Construye una lista de calificaciones
    if len(p) == 2:
        p[0] = [int(p[1])]  # Una sola calificación
    else:
        p[0] = [int(p[1])] + p[3]  # Varias calificaciones

def p_average(p):
    'F : key_average colon number_value'
    # Procesa el promedio del alumno
    p[0] = {"average": float(p[3])}

# Regla para manejar errores
def p_error(p):
    print("Syntax error at", p.value if p else "EOF")

# Construir el parser
parser = yacc.yacc()

# Leer y procesar el archivo JSON
if __name__ == '__main__':
    with open('input.json', 'r') as json_file:
        json_string = json_file.read()

    print("\n------ Parsing the JSON Data ------")
    try:
        result = parser.parse(json_string)
        print("\n------ Parsed Data ------\n", result)

        # Exportar los datos a CSV
        if result:
            with open("grades.csv", "w") as archivo:
                archivo.write("ID,Name,Course,Grades,Average\n")
                for alumno in result:
                    grades_str = ";".join(map(str, alumno['grades']))
                    archivo.write(f"{alumno['id']},{alumno['name']},{alumno['course']},{grades_str},{alumno['average']}\n")
            print("\nData successfully exported to grades.csv!")
    except Exception as e:
        print("Error during parsing:", e)
