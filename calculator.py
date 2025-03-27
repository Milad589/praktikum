def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y 

def divi(x, y):
    if y == "0":
        raise ZeroDivisionError
    return compute

def message(msg):
    print("\n=== " + str(msg) + " ===\n")

def compute(op, x, y):
    #print(type(op), type(x), type(y))
    result = 0
    if op == "*":
        result = multi(x, y)
    elif op == "+":
        result = add(x, y)
    elif op == "-":
        result = sub(x, y)
    elif op == "/":
        result = divi(x, y)
    return result
 
def main():
    while True:
        try:
            erlaubte_operatoren = ["+","-","*","/"]
            op = input("Operator (+, -, *, /) or q for leave: ")
            if op == "q":
                message("Programm Beendet")
                exit(0)
 
            if op in erlaubte_operatoren:
                a = float(input("Erste Zahl: "))
                b = float(input("Zweite Zahl: "))
                message("Das Ergebnis lautet: " + str(result))
            else:
                message("Ungültiger Operator gültige Operatoren sind +,-,/,*")
       
        except ZeroDivisionError:
            message("Division durch null nicht möglcih")
        except ValueError:
            message("Bitte eine gültige Zahl eingeben.")
 
if __name__ == '__main__':
    main()






    