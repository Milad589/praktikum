import logging
from mylog import message


def compute(op, a, b):
    """
    Führt eine Berechnung basierend auf dem Operator und den Operanden durch.

    Args:
        op (str): Der Operator, der die Art der Berechnung angibt (+, -, *, /).
        a (float): Der erste Operand.
        b (float): Der zweite Operand.

    Returns:
        float: Das Ergebnis der Berechnung.

    Raises:
        ZeroDivisionError: Wenn der Operator "/" ist und b gleich 0 ist.
    """
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


