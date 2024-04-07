import LogicalOperators

def generate_truth_table(expression):
    mymap = {" ":"",
            "not":"!", "~": "!", 
            "and" : "&", "xor":"^" ,"or": "|",
            "biimplies": "<", "<=>":"<",
            "implies":">" , "=>":">" , "->":">"
            }

    for key,value in mymap.items():
        expression = expression.replace(key,value)
    
    variables = extract_variables(expression)  # Extract variables from the expression
    table = generate_table_header(variables, expression)  # Generate table header

    values = generate_truth_values(variables)  # Generate all possible truth values

    for row in values:
        result = evaluate_expression(expression, variables, row)  # Evaluate the expression for each truth value combination
        row.append(result)  # Append the expression result to the row
        table.append(row)  # Add the row to the table

    return table

def extract_variables(expression):
    variables = []
    for char in expression:
        if char.isalpha() and char not in variables:
            variables.append(char)
    return variables

def generate_table_header(variables, expression):
    header = variables.copy()
    header.append(expression)
    return [header]

def generate_truth_values(variables):
    values = []
    rows = 2 ** len(variables)

    for i in range(rows - 1,-1,-1):
        row = []
        for j in range(len(variables) - 1,-1,-1):
            value = (i >> j) & 1
            row.append(bool(value))
        values.append(row)

    return values

def evaluate_expression(expression, variables, values):
    evaluation = expression
    for variable, value in zip(variables, values):
        evaluation = evaluation.replace(variable, str(int(value)))
    return bool(LogicalOperators.evaluate(evaluation))

# Example usage
simplified_expression = "h and not a xor b"
truth_table = generate_truth_table(simplified_expression)
# Printing the truth table
print("Truth Table:")
for row in truth_table:
    print("\t".join(map(str, row)))
