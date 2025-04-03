import sys
import mylog
import argparse
from right import compute_expression  

def parse_arguments():
    """Parst die Kommandozeilenargumente und gibt sie zurück."""
    parser = argparse.ArgumentParser(description="Berechnet einen mathematischen Ausdruck.")
    parser.add_argument("expression", type=str, nargs="?", help="Der mathematische Ausdruck, der berechnet werden soll.")
    parser.add_argument("-l", "--logfile", type=str, help="Optionales Logfile für die Ausgaben.")
    return parser.parse_args()

def main():
    """Hauptfunktion zur Berechnung eines mathematischen Ausdrucks."""
    args = parse_arguments()
    
    if args.logfile:
        mylog.mylog(args.logfile)
    else:
        mylog.mylog("milad.bib")
    
    if not args.expression:
        mylog.message("error", "Kein mathematischer Ausdruck angegeben.")
        sys.exit("Fehler: Bitte einen mathematischen Ausdruck angeben.")
    
    expression = args.expression
    mylog.message("info", f"Berechnungsausdruck: {expression}")
    
    try:
        result = compute_expression(expression)
        print(f"\n=== Das Ergebnis lautet: {result} ===\n")
    except ZeroDivisionError:
        mylog.message("error", "Division durch Null ist nicht erlaubt.")
        sys.exit("\n=== Fehler: Division durch Null ist nicht erlaubt! ===\n")
    except ValueError:
        mylog.message("error", "Ungültiger mathematischer Ausdruck.")
        sys.exit("\n=== Fehler: Ungültiger mathematischer Ausdruck! ===\n")
    except Exception as e:
        mylog.message("error", f"Unerwarteter Fehler: {e}")
        sys.exit(f"\n=== Ein unerwarteter Fehler ist aufgetreten: {e} ===\n")

if __name__ == "__main__":
    main()
