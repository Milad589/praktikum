def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    if y == "0":
        raise ZeroDivisionError
    return x / y




while True:
    try:
        a = float(input("Erste Zahl: "))
        op = input("Operator (+, -, *, /): ")
        b = float(input("Zweite Zahl: "))
        
        if op == "*":
            result = multi(a, b)
            print("Das Ergebnis ist:", result) 
        elif op == "+":
            result = add(a, b)
            print("Das Ergebnis ist:", result) 
        elif op == "-":
            result = sub(a, b)    
            print("Das Ergebnis ist:", result) 
        elif op == "/":
            result = divi(a, b)
            print("Das Ergebnis ist:", result)      
        else:
            print("ungültiger Operator gültige Operator sind: +, -, *, /")    
    except ZeroDivisionError:
        print("Division durch null nicht möglcih")
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")






    