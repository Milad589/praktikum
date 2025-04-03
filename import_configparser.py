import configparser
import os

class ConfigLoader:
    def __init__(self, config_file=".env.cfg"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

    def load_config(self):
        # Überprüfen, ob die Datei existiert
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Die Konfigurationsdatei '{self.config_file}' wurde nicht gefunden.")

        # Datei einlesen
        self.config.read(self.config_file)

    def get(self, section, key, fallback=None):
        # Wert aus einer bestimmten Sektion abrufen
        if section in self.config and key in self.config[section]:
            return self.config[section][key]
        return fallback

    def get_all(self):
        # Alle Variablen als Dictionary zurückgeben
        config_dict = {}
        for section in self.config.sections():
            config_dict[section] = dict(self.config[section])
        return config_dict