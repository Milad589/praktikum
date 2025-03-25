def add_numbers():
    """
    Diese Funktion erlaubt die Eingabe von zwei Zahlen, addiert sie und gibt das Ergebnis aus.
    """
    try:
        # Eingabe der ersten Zahl
        num1 = float(input("Geben Sie die erste Zahl ein: "))
        # Eingabe der zweiten Zahl
        num2 = float(input("Geben Sie die zweite Zahl ein: "))
       
        # Addition der beiden Zahlen
        result = num1 + num2
       
        # Ausgabe des Ergebnisses
        print(f"Das Ergebnis der Addition von {num1} und {num2} ist: {result}")
    except ValueError:
        print("Ungültige Eingabe! Bitte geben Sie gültige Zahlen ein.")
 
# Hauptprogramm
if __name__ == "__main__":
    add_numbers()