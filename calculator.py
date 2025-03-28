import logging

logging.basicConfig(level=logging.INFO, filename="logs.txt", filemode='w', format='%(asctime)s - %(message)s')

def message(msg):
    logging.info(msg)

def compute(op, a, b):
    message("Berechne: " + str(a) + " " + op + " " + str(b))
    
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Division durch Null!")
        result = a / b
    
    message("Ergebnis: " + str(result))
    return result

def main():
    while True:
        try:
            valid_operators = ["+", "-", "*", "/"]
            op = input("Operator (+, -, *, /) oder q zum Verlassen: ")
            
            if op == "q":
                message("Programm Beendet")
                print("Programm Beendet")
                exit(0)

            if op in valid_operators:
                a = float(input("Erste Zahl: "))
                b = float(input("Zweite Zahl: "))
                
                message("Operator: " + op + ", Erste Zahl: " + str(a) + ", Zweite Zahl: " + str(b))
                
                result = compute(op, a, b)
                
                print("\n=== Das Ergebnis der Berechnung lautet: " + str(result) + " ===\n")
            else:
                message("Ungültiger Operator! Gültige Operatoren sind: +, -, *, /")

        except ZeroDivisionError as e:
            message("Fehler: " + str(e))
            print("\n=== Fehler: Division durch Null ist nicht möglich! ===\n")
        except ValueError:
            message("Fehler: Bitte eine gültige Zahl eingeben!")
            print("\n=== Fehler: Bitte eine gültige Zahl eingeben! ===\n")

if __name__ == "__main__":
    main()

