# Ein-/Ausgabe

# input
# Wartet auf eine Eingabe durch den User
# Kann einen Text präsentieren

# eingabe = input("Gib eine Zahl ein: ")
# print(f"Deine Zahl ist: {eingabe}")
# # print(f"Deine Zahl mal Zwei ist: {eingabe * 2}")  # Hier wird eine String-Multiplikation durchgeführt -> Umwandlung
#
# eingabeZahl = 0
# if eingabe.isnumeric():
# 	eingabeZahl = int(eingabe)
# print(f"Deine Zahl mal Zwei ist: {eingabeZahl * 2}")

# Escape-Sequenzen
# Undruckbare Zeichen in einen String einbauen
# \n: Zeilenumbruch
# \t: Tabulator
# \\: Einzelner Backslash
# \u + 4 Ziffern: beliebiger Unicode Character
# https://docs.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170

#################################################################################

# open
# Datei lesen/schreiben
# Benötigt einen Pfad und einen Modus
# Modi: R, W, A
file = open("Test.txt", "w")
file.write("Hallo")  # Hier wird Hallo nur in den Buffer geschrieben
file.flush()  # Flush schreibt den Inhalt in die unterliegende Datei
file.close()  # WICHTIG: Stream am Ende schließen


read = open("Test.txt", "r")
zeile = read.readline()  # Einzelne Zeile lesen
print(f"Inhalt: {zeile}")

# read.readline() lässt die Position des unterliegenden Streams am Ende des Files
# seek setzt die Position an eine bestimmte Stelle (hier 0 = Anfang)
read.seek(0)
zeilen = read.readlines()  # Alle Zeilen lesen
print(f"Inhalt: {zeilen}")
read.close()

#################################################################################

# with-Block
# Schließt den Stream am Ende des Blocks automatisch
# Macht auch automatisch Flush, da Close beim File automatisch Flush beinhält
# Sollte generell bei Files verwendet werden

with open("Test.txt", "w") as f:
	f.write("Hallo vom with-Block")

#################################################################################

# rstring
# String, welcher Escape-Sequenzen ignoriert
# pfad = "C:\Users\lk3\source\repos\Python_Grundkurs_2024_06_05\venv\Scripts"  # Jedes Pfadtrennzeichen wird hier als ES interpretiert
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2024_06_05\venv\Scripts"

# Das os Modul
# Enthält verschiedene Funktionen die mit dem Betriebssystem zusammenhängen
# Enthält u.a. Pfadoperation
import os
if os.path.exists("Test.txt"):
	print("File existiert bereits")
print(os.path.join("Das", "ist", "ein", "Pfad"))

#################################################################################

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Bei w oder a soll ein File geöffnet werden und eine Erfolgsmeldung in das File geschrieben werden
# Bei r soll das File ausgelesen werden und der Inhalt in die Konsole geschrieben werden

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Rechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Rechnung (Wiederholen) durchführen will
