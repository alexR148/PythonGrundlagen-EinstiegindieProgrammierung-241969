# Module
# Sind normale Python Skripte die in andere Python Skripte eingebunden werden können
# WICHTIG: Wenn ein Skript importiert wird, wird es komplett ausgeführt

# Skripte importieren mittels import
# Syntax: import <Name>
import M001
print("M001 importiert")  # ACHTUNG: Gesamtes Skript wird hier ausgeführt

print(M001.x)  # In andere Skripte hineingreifen mit <Name>.<Variable/Funktion/Klasse/...>

# Aliases mit as (vorallem nützlich bei langen Skriptnamen)
import M006 as M

print(M.countCase("Das ist ein Text"))

# from-Import
# Normalerweise wird bei import alles aus dem Skript importiert
# Mit dem from-Import können nur bestimmte Member importiert werden
# ACHTUNG: Gesamtes Skript wird hier ausgeführt
from M006 import countCase, listTeilnehmer, maximum  # Nur die drei gegebenen Funktionen importieren
listTeilnehmer("T1", "T2", "T3")  # Hier muss der Name des Skripts nicht angegeben werden

from M006 import *  # Bindet alles aus dem gegebenen Skript ein (Vorteil: Name des Moduls muss garnicht mehr verwendet werden)

#######################################################################

# Wo werden Module beim Import gesucht?
import sys
for pfad in sys.path:
	print(pfad)

# 1. Im selben Verzeichnis wie das Skript
# 2. In der Standardinstallation
# 3. In der venv (externe Pakete)
# 4. (optional) Eigene Pfade
# sys.path.append("...")
# Wenn Modul nicht gefunden wird: ModuleNotFoundError

# Externe Module installieren
# Zwei Möglichkeiten
# Über Python Packages
# Über pip
# - pip install <Name>
# - pip uninstall <Name>
# pip aktualisieren: py -m ensurepip --upgrade

# Externe Pakete importieren:
# import numpy

#######################################################################

# Die Main Methode
# Der Startpunkt des Skripts

# __name__
# Der Name des Skripts bei Import (M007) oder falls das Skript direkt gestartet wird: __main__
print(__name__)

def main():
	pass

# Der Startpunkt eines Python Skripts
if __name__ == "__main__":
	main()
	# Initialcode...

#######################################################################

# Packages
# Sind nur Ordner, die Python Skripte enthalten
# Können als Gesamtpaket importiert werden

# Gesamt:
# import M007c

# Einzelteile:
# from M007c import M007_Test as T

# __init__.py
# Wird bei einem Gesamtimport von einem Package (Ordner) ausgeführt