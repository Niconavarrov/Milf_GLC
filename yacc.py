import ply.yacc as yacc
from lexer import tokens  # Import tokens from the lexer

# Grammar rules
def p_start(p):
    'S : sbracket A sbracketF'
    p[0] = p[2]

def p_multiple_records(p):
    'A : curlyb B curlybF comma A'
    p[0] = [p[2]] + p[5]

def p_single_record(p):
    'A : curlyb B curlybF'
    p[0] = [p[2]]

def p_record_structure(p):
    'B : key_id colon number_value comma C'
    record = {"id": int(p[3])}
    record.update(p[5])
    p[0] = record

def p_name(p):
    'C : key_name colon string_value comma D'
    record = {"name": p[3].strip('"')}
    record.update(p[5])
    p[0] = record

def p_course(p):
    'D : key_course colon string_value comma E'
    record = {"course": p[3].strip('"')}
    record.update(p[5])
    p[0] = record

def p_grades(p):
    'E : key_grades colon sbracket G sbracketF comma F'
    record = {"grades": p[4]}
    record.update(p[7])
    p[0] = record

def p_grade_list(p):
    '''G : number_value
         | number_value comma G'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_average(p):
    'F : key_average colon number_value'
    p[0] = {"average": float(p[3])}

def p_error(p):
    print("Syntax error at", p.value if p else "EOF")

# Build the parser
parser = yacc.yacc()

# Main program
if __name__ == '__main__':
    try:
        with open('input.json', 'r', encoding='utf-8') as json_file:
            json_string = json_file.read()

        print("\n------ Parsing the JSON Data ------")
        result = parser.parse(json_string)
        print("\n------ Parsed Data ------\n", result)

        # Export parsed data to CSV
        if result:
            with open("grades.csv", "w") as csv_file:
                csv_file.write("ID,Name,Course,Grades,Average\n")
                for record in result:
                    grades_str = ";".join(map(str, record['grades']))
                    csv_file.write(f"{record['id']},{record['name']},{record['course']},{grades_str},{record['average']}\n")
            print("\nData successfully exported to grades.csv!")
    except Exception as e:
        print("Error during parsing:", e)
