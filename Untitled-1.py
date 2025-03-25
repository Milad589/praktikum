
def rechne(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError
        return a / b
    else:
        raise ValueError("Ungültiger Operator")

def benutzereingabe():
    a = float(input("Erste Zahl: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Zweite Zahl: "))
    return a, b, op

while True:
    try:
        a, b, op = benutzereingabe()  # Benutzer-Eingabe wird durch Funktion vereinfacht
        result = rechne(a, b, op)    # Berechnung in einer Funktion
        print(f"Ergebnis: {result}")
    except ZeroDivisionError:
        print("Division durch null nicht möglich")
    except ValueError as e:
        print(e)  # Zeigt die Fehlermeldung für ungültigen Operator oder Zahleneingabe
