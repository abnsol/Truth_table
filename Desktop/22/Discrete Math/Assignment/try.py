import sys

def truth_table(expression,inputs):
    expression = expression.replace(" ","")
    finalTable = []

    variables = extractVariables(expression)
    header = createHeader(variables,expression)
    finalTable.append(header)

    values = truthValues(variables)
    for row in values:
        evaluated = evaluateValues(row,expression,variables)
        row.append(evaluated)
    finalTable.append(values)

    print("Truth Table: ")
    print()
    for rows in finalTable:
        for row in rows:
            print("  |  ".join(map(str,row)),end = "|\n")
            print("-----" * len(row))


def extractVariables(expression):
    variables = []
    for char in expression:
        if char.isalpha() and char not in variables:
            variables.append(char)
    return variables

def createHeader(variable,expression):
    header = [] + variable + [expression]
    return [header]

def truthValues(variable):
    values = []
    rows = 2 ** len(variable)

    for i in range(rows):
        row = []
        for j in range(len(variable)):
            val = (i >> j) & 1
            row.append(val)
        values.append(row)
    
    return values

def evaluateValues(row,expression,variables):
    temp = expression
    for val,var in zip(row,variables):
        temp = temp.replace(var,str(val))
    ans = eval(temp)
    return int(ans)

expression = input("Expression: ")
inputs = int(input("inputs: "))
truth_table(expression,inputs)



