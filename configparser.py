import os
import import_configparser


# Beispielnutzung
if __name__ == "__main__":
    # Erstelle eine Instanz des ConfigLoaders
    config_loader = import_configparser.ConfigLoader(".env.cfg")

    try:
        # Konfigurationsdatei laden
        config_loader.load_config()

        # Einzelne Variable abrufen
        logf = config_loader.get("LOG", "logfile", fallback="Keine LOG-Section gefunden")
        print(f"LOG: {logf}")

        mpass = config_loader.get("MILAD", "milad_password", fallback="Keine MILAD-Section gefunden")
        print(f"Milads Password: {mpass}")
    except FileNotFoundError as e:
        print(e)