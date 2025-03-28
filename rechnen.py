import logging
from mylog import message

def compute(op, a, b):
    """Führt eine Berechnung durch und loggt das Ergebnis."""
    message("info", "Berechne: " + str(a) + " " + op + " " + str(b))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            message("error", "Division durch Null!")
            raise ZeroDivisionError("Division durch Null!")
        result = a / b

    message("info", "Ergebnis: " + str(result))
    return result