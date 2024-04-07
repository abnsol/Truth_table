import re
symbols = {" ": "", "not":"!", "and" : "&", "xor":"^" ,"or": "|","biimplies": "=", "implies":"_"}

expression = input("Expression: ")
inputs = int(input("Number of variable: "))
for key,value in symbols.items():
    expression = expression.replace(key,value)

def neg(a):
    return (~a) & 1
def con(a,b):
    return a & b
def dis(a,b):
    return a | b
def excl(a,b):
    return a ^ b
def implication(a,b):
    return neg(a) | b
def bi(a,b):
    return int(a == b)

def postfix(temp):
    def prec(c):
        if c == '~':  # Negation
            return 4
        elif c == '&':  # Logical AND
            return 3
        elif c == '|':  # Logical OR
            return 2
        elif c == '^':  # Logical XOR
            return 2
        elif c == '=':  # Biimplication
            return 1
        else:
            return -1

    def associativity(c):
        if c == '~':  # Negation is right-associative
            return 'R'
        return 'L'  # Default to left-associative

    def infix_to_postfix(s):
        result = []
        stack = []

        for i in range(len(s)):
            c = s[i]

            # If the scanned character is an operand, add it to the output string.
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                result.append(c)
            # If the scanned character is an ‘(‘, push it to the stack.
            elif c == '(':
                stack.append(c)
            # If the scanned character is an ‘)’, pop and add to the output string from the stack
            # until an ‘(‘ is encountered.
            elif c == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # Pop '('
            # If an operator is scanned
            else:
                while stack and (prec(s[i]) < prec(stack[-1]) or
                                (prec(s[i]) == prec(stack[-1]) and associativity(s[i]) == 'L')):
                    result.append(stack.pop())
                stack.append(c)

        # Pop all the remaining elements from the stack
        while stack:
            result.append(stack.pop())

        return ''.join(result)
    
    return infix_to_postfix(temp)

def evaluate_postfix(exp):
    stack = []

    for i in exp:
        # If the character is an operand, push it onto the stack
        if i.isdigit():
            stack.append(i)
        # If the character is an operator
        else:
            # Pop the top two elements from the stack
            val1 = stack.pop()
            val2 = stack.pop()
            # Apply the operator to the operands and push the result back onto the stack
            if i == '&':  # Logical AND
                val = con(val1,val2)
                stack.append(str(val))
            elif i == '|':  # Logical OR
                val = dis(val1,val2)
                stack.append(str(val))
            elif i == '^':  # Logical XOR
                val = excl(val1,val2)
                stack.append(str(val))
            elif i == '~':  # Logical NOT (Negation)
                val = neg(val1)
                stack.append(str(val))
            elif i == '=':  # Biimplication
                val = bi(val1,val2)
                stack.append(str(val))
            elif i == '_':
                val = implication(val1,val2)
            # You can add more operators here if needed
    # The final result is the top element of the stack
    return int(stack.pop())

# Example usage
res = postfix(expression)
result = evaluate_postfix(res)

print(result)




