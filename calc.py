import sys
import mylog
from right import compute_expression  

def main():
    """Berechnet einen mathematischen Ausdruck aus den Kommandozeilenargumenten."""
    
    
    if len(sys.argv) != 2:
        sys.exit("Fehler: Bitte genau einen mathematischen Ausdruck als Argument übergeben.")
    
    expression = sys.argv[1]
    mylog.message("info", "Berechnungsausdruck: " + expression)
    
    try:
       
        result = compute_expression(expression)
        print("\n=== Das Ergebnis lautet: " + str(result) + " ===\n")
    
    except ZeroDivisionError:
        sys.exit("\n=== Fehler: Division durch Null ist nicht erlaubt! ===\n")
    except ValueError:
        sys.exit("\n=== Fehler: Ungültiger mathematischer Ausdruck! ===\n")
    except Exception as e:
        sys.exit("\n=== Ein unerwarteter Fehler ist aufgetreten: " + str(e) + " ===\n")

if __name__ == "__main__":
    mylog.mylog("milad.bib")  
    main()