from collections import defaultdict
exp = "0>1&0<0|1^~1<1"

def evaluate(string):
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
            elif string[i] == "~": symbols[6].append(i)

    print(sorted(symbols.items()))

    if len(string) == 1:
        return int(string)
    else:
        if len(symbols[1]) != 0:
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
            else: return 0
print(evaluate(exp))