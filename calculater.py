import logging
import mylog
from rechnen import compute  

def main():
    """Hauptprogramm, das die Benutzerinteraktion übernimmt.
    Fragt den Benutzer nach Eingaben, führt Berechnungen durch und zeigt Ergebnisse"""
    while True:
        try:
            valid_operators = ["+", "-", "*", "/"]
            op = input("Operator (+, -, *, /) oder q zum Verlassen: ")
            
            if op == "q":
                mylog.message("info", "Programm Beendet")
                print("Programm Beendet")
                exit(0)

            if op in valid_operators:
                a = float(input("Erste Zahl: "))
                b = float(input("Zweite Zahl: "))
                
                mylog.message("info", "Operator: " + op + ", Erste Zahl: " + str(a) + ", Zweite Zahl: " + str(b))
                
                result = compute(op, a, b)  
                
                print("\n=== Das Ergebnis der Berechnung lautet: " + str(result) + " ===\n")
            else:
                mylog.message("error", "Ungültiger Operator! Gültige Operatoren sind: +, -, *, /")
                print("Ungültiger Operator! Gültige Operatoren sind: +, -, *, /")

        except ZeroDivisionError as e:
            mylog.message("error", "Fehler: " + str(e))
            print("\n=== Fehler: Division durch Null ist nicht möglich! ===\n")
        except ValueError:
            mylog.message("error", "Fehler: Bitte eine gültige Zahl eingeben!")
            print("\n=== Fehler: Bitte eine gültige Zahl eingeben! ===\n")

if __name__ == "__main__":
    mylog.mylog("milad.bib")  
    main()