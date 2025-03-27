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

def compute(op, x, y):
    result = 0
    if op == "*":
        resukt = multi(x, y)
    elif op == "+":
        resukt = add(x, y)
    elif op == "-":
        result = sub(x, y)
    elif op == "/":
        result = divi(x, y)
    return result



while True:
    try:
        op = input("Operator (+, -, *, /): ")
        if op == "q":
            exit(0)

        a = float(input("Erste Zahl: "))
        b = float(input("Zweite Zahl: "))
        
        
        print("Das Ergebnis lautet:", compute(op, a, b))
    except ZeroDivisionError:
        print("Division durch null nicht möglcih")
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")






    