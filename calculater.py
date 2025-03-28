import logging
import mylog
from rechnen import compute  

def message(Loglevel, msg):
    """
    Loggt eine Nachricht mit dem angegebenen Log-Level.
    """
    loglevel = Loglevel.lower()
    if loglevel == "info":
        logging.info(msg)
    elif loglevel == "error":
        logging.error(msg)
    elif loglevel == "warning":
        logging.warning(msg)
    elif loglevel == "debug":
        logging.debug(msg)
    else:
        logging.info("Unbekanntes Loglevel: " + msg)

def main():
    """Hauptprogramm, das die Benutzerinteraktion übernimmt.
    Fragt den Benutzer nach Eingaben, führt Berechnungen durch und zeigt Ergebnisse"""
    while True:
        try:
            valid_operators = ["+", "-", "*", "/"]
            op = input("Operator (+, -, *, /) oder q zum Verlassen: ")
            
            if op == "q":
                message("info", "Programm Beendet")
                print("Programm Beendet")
                exit(0)

            if op in valid_operators:
                a = float(input("Erste Zahl: "))
                b = float(input("Zweite Zahl: "))
                
                message("info", "Operator: " + op + ", Erste Zahl: " + str(a) + ", Zweite Zahl: " + str(b))
                
                result = compute(op, a, b)  
                
                print("\n=== Das Ergebnis der Berechnung lautet: " + str(result) + " ===\n")
            else:
                message("error", "Ungültiger Operator! Gültige Operatoren sind: +, -, *, /")
                print("Ungültiger Operator! Gültige Operatoren sind: +, -, *, /")

        except ZeroDivisionError as e:
            message("error", "Fehler: " + str(e))
            print("\n=== Fehler: Division durch Null ist nicht möglich! ===\n")
        except ValueError:
            message("error", "Fehler: Bitte eine gültige Zahl eingeben!")
            print("\n=== Fehler: Bitte eine gültige Zahl eingeben! ===\n")

if __name__ == "__main__":
    mylog.mylog("milad.bib")  
    main()