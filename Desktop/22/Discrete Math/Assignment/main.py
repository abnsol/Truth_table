import LogicalOperators
import Truth_Table
import sys

def guide():
    print("""Hi🖐  there!
This is a program that assists you with evaluating logical operations and it also generates truth tables.
While using this program you must use valid operators which are listed below

Operators:
For Negation -> negation , not, ~ , !
For Conjunction -> and , &
For Disjunction -> or , |
For ExclusiveOR -> xor , ^
For Implication -> implies , =>, ->
For Biimplication -> biimplies , <=> , ==

- The program supports any number of inputs including parenthesis.
Enter 1 to continue: """, end = '')
    
def menu():
    print("""\nEnter 1 : If you want to calculate single operation.
Enter 2 : If you want to generate truth table.
Enter 3 : If you want to go back to the guide.
Enter 4 : If you want to exit the program.""")
    choice = int(input("\nChoice: "))
    if choice == 1:
        expression = input("\nEnter Expression: ")
        print("The solution for ",expression," is ",LogicalOperators.evaluate(expression))
        menu()
    elif choice == 2:
        print("\nEnter expression: ",end = '')
        expression = input()
        print()
        Truth_Table.truth_table(expression)
        menu()
    elif choice == 3:
        guide()
        menu()
    elif choice == 4:
        sys.exit("\nThank you for using the program!")

guide()
a = int(input())
while a != 1:
    guide()

menu()

