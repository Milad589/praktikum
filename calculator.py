import logging

logging.basicConfig(level=logging.INFO, filename="logs.py")

def message(msg):
    logging.info(msg)
    print("\n=== " + str(msg) + " ===\n")

def compute(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b

def main():
    while True:
        try:
            erlaubte_operatoren = ["+", "-", "*", "/"]
            op = input("Operator (+, -, *, /) oder q zum Verlassen: ")
            if op == "q":
                message("Programm beendet")
                exit(0)

            if op in erlaubte_operatoren:
                a = float(input("Erste Zahl: "))
                b = float(input("Zweite Zahl: "))
                message("Das Ergebnis lautet: " + str(compute(op, a, b)))
            else:
                message("Ungültiger Operator! Gültige Operatoren sind: +, -, *, /")

        except ZeroDivisionError:
            message("Fehler: Division durch Null ist nicht möglich!")
        except ValueError:
            message("Fehler: Bitte eine gültige Zahl eingeben!")

if __name__ == "__main__":
    main()





    