from collections import defaultdict

def evaluate(string):
    mymap = {" ":"",
            "not":"!", "~": "!", 
            "and" : "&", "xor":"^" ,"or": "|",
            "biimplies": "<", "<=>":"<",
            "implies":">" , "=>":">" , "->":">"
            }

    for key,value in mymap.items():
        string = string.replace(key,value)
        
    symbols = defaultdict(list)  

    for i in range(len(string)):
        if string[i].isdigit():
            continue
        else:
            if string[i] == "<": symbols[1].append(i)
            elif string[i] == ">": symbols[2].append(i)
            elif string[i] == "^": symbols[3].append(i)
            elif string[i] == "|": symbols[4].append(i)
            elif string[i] == "&": symbols[5].append(i)
            elif string[i] == "!": symbols[6].append(i)
            elif string[i] == "(": symbols[7].append(i)

    # evaluating using recursion
    if len(string) == 1:
        return int(string)
    else:

        if len(symbols[7]) != 0:
            # to know where our parenthesis start and end
            idx = symbols[7][0] + 1
            openbracket = 1
            closebracket = 0
            while closebracket < openbracket:
                if string[idx] == ')':
                    closebracket += 1
                elif string[idx] == '(':
                    openbracket += 1
                idx += 1
            
            # after finding our parenthesis evaluate inside the parenthesis and assign it to val
            val = evaluate(string[(symbols[7][0] + 1) : idx - 1])

            # form a newstring that removes solved parenthesis 
            if idx == len(string):
                newstring = string[:symbols[7][0]] + str(val) 
            else:
                newstring = string[:symbols[7][0]] + str(val) + string[idx:]

            # call evaluate function to solve the newstring   
            return evaluate(newstring)

        
        elif len(symbols[1]) != 0:
            return int(evaluate(string[0:symbols[1][0]]) == evaluate(string[(symbols[1][0] + 1):(symbols[1][0] + (len(string) - symbols[1][0]))]))
        
        elif len(symbols[2]) != 0:
            temp = evaluate(string[0:symbols[2][0]])
            if temp == 1: temp = 0
            else: temp = 1
            return temp | evaluate(string[(symbols[2][0] + 1):(symbols[2][0] + (len(string) - symbols[2][0]))])
        
        elif len(symbols[3]) != 0:
            return evaluate(string[0:symbols[3][0]]) ^ evaluate((string[(symbols[3][0] + 1) : symbols[3][0] + (len(string) - symbols[3][0])]))
        
        elif len(symbols[4]) != 0:
            return evaluate(string[0:symbols[4][0]]) | evaluate((string[(symbols[4][0] + 1) : symbols[4][0] + (len(string) - symbols[4][0])]))
        
        elif len(symbols[5]) != 0:
            return evaluate(string[0:symbols[5][0]]) & evaluate((string[(symbols[5][0] + 1) : symbols[5][0] + (len(string) - symbols[5][0])]))
        
        elif len(symbols[6]) != 0:
            if string[symbols[6][0] + 1] == '0':
                return 1
            else : return 0

def minterms(values):
    exp = ""
    for i in range(len(values)):
        if i == len(values) - 1:
            if values[i] == True:
                exp += str(int(values[i]))
            else:
                complement = "!" + str(int(values[i]))
                exp += str(evaluate(complement))
        else:
            if values[i] == True:
                exp += str(int(values[i]))
                exp += "&"
            else:
                complement = "!" + str(int(values[i]))
                exp += str(evaluate(complement))
                exp += "&"

    return evaluate(exp)

def maxterms(values):
    exp = ""
    for i in range(len(values)):
        if i == len(values) - 1:
            if values[i] == False:
                exp += str(int(values[i]))
            else:
                complement = "!" + str(int(values[i]))
                exp += str(evaluate(complement))
        else:
            if values[i] == False:
                exp += str(int(values[i]))
                exp += "|"
            else:
                complement = "!" + str(int(values[i]))
                exp += str(evaluate(complement))
                exp += "|"
        
    return evaluate(exp)

def SOP(table,expression):
    arr = []
    for row in range(1,len(table)): 
        if table[row][-1] == 1:
            arr.append(row)
    print("SOP(",expression," ) = Summation",arr)

def POS(table,expression):
    arr = []
    for row in range(1,len(table)):
        if table[row][-1] == 0:
            arr.append(row)
    print("POS(",expression,") = Product",arr)
