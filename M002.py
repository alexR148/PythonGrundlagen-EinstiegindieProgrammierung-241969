# List
# Sammlung von Elementen
# Mehrere Werte in einer Variable statt nur einem
# Die List wird mit [] definiert
# Kann einen Index benutzen
# Kann Duplikate enthalten
# Kann verschiedene Datentypen enthalten
meineListe = [1, 2, 3, 4]
print(meineListe)

# append: Neue Elemente hinzufügen
meineListe.append(10)
print(meineListe)

# pop: Element an einem Index entfernen
meineListe.pop(3)
print(meineListe)

# remove: Sucht das gegebene Element und entfernt es
meineListe.remove(10)  # Entfernt die erste 10
print(meineListe)

# Aufgabenstellung: Liste1 und Liste2 zusammenbauen
meineListe2 = ["Hallo", "Welt"]
meineListe.append(meineListe2)  # Verschachtelte Liste
print(meineListe)

meineListe.remove(meineListe2)

# extend: Nimmt die Elemente aus der gegebenenen Liste und fügt diese in die erste Liste ein
meineListe.extend(meineListe2)
print(meineListe)

# Alternative:
meineListe += meineListe2
print(meineListe)

# sort: Sortiert die Liste
# meineListe.sort()  # Liste mit gemischten Typen kann nicht sortiert werden
zahlen = [5, 2, 4, 1, 2, 1, 9, 5]
zahlen.sort()
print(zahlen)

zahlen.sort(reverse=True)  # Absteigend sortieren
print(zahlen)

# Index bei Liste (wie bei String)
print(zahlen[3])
print(zahlen[3:7])
print(zahlen[-2])

####################################################################

# Tuple
# Funktioniert wie List, kann aber nicht verändert werden
# Hat auch Index, wird mit () definiert
meinTupel = (2, 3, 4, 5)
print(meinTupel)  # In der Konsole anhand der Klammern kann der Typ der Liste determiniert werden

# Tupel über Umweg verändern
meinTupel = list(meinTupel)  # Konvertierung zu einer Liste
meinTupel.append(1)  # Neuer Wert einfügen
meinTupel = tuple(meinTupel)  # Zurückkonvertierung
print(meinTupel)

####################################################################

# range
# Bereich von X bis Y
bis100 = range(100)
print(bis100)  # Hier wird nur ein Generator erzeugt, welcher bereit ist Werte zu erzeugen
print(list(bis100))  # Mit einer Konvertierung zu List/Tuple kann das Erzeugen gestartet werden

bis100m = range(100_000_000)
print(bis100m)
# x = list(bis100m)  # Hier werden die Werte konkret erzeugt, hier werden Resourcen verbraucht (RAM, CPU)

print(list(range(-50, 50)))  # Bereich von -50 bis 49

print(list(range(0, 100, 5)))  # Bereich von 0 bis 100 mit 5er Schritten (0, 5, 10, 15, ...)
print(list(range(0, 101, 5)))  # 100 inkludieren

####################################################################

# Set
# Funktioniert wie List, aber Duplikate sind nicht erlaubt
meinSet = {1, 2, 3, 4, 5}  # Set mit {} Klammern
print(meinSet)

meinSet.add(5)  # Kein Effekt
meinSet.add(6)  # 6 wird hinzugefügt
print(meinSet)

# discard: Effektiv Remove
meinSet.discard(1)
print(meinSet)

# Anwendungsfall: Duplikate filtern
duplikate = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8]
print(set(duplikate))  # Liste zu Set konvertieren
duplikate = list(set(duplikate))
print(duplikate)

####################################################################

# Dictionary
# Funktioniert wie Set, aber jedes Element hat einen Namen (Schlüssel)
meinAuto = {
	"Marke": "Audi",
	"Modell": "A3",
	"Baujahr": 2020
}

# meinAutoSet = {"Audi", "A3", 2020}  # Hier kann nicht determiniert werden, für was die Einträge stehen

# Elemente angreifen: Index
print(meinAuto["Marke"])
print(meinAuto["Modell"])
print(meinAuto["Baujahr"])

# Wert verändern
meinAuto["Baujahr"] = 2010
print(meinAuto)

# Neuen Wert hinzufügen oder verändern
meinAuto["KM"] = 50_000
print(meinAuto)

# Neuen Wert hinzufügen wenn er noch nicht vorhanden ist
if meinAuto.get("KM") is None:
	meinAuto["KM"] = 100_000
print(meinAuto)

# pop: Schlüssel entfernen
meinAuto.pop("Marke")
print(meinAuto)

# Gesamtes Objekt entfernen
# meinAuto = None
# print(meinAuto)

# Nur Schlüssel, nur Werte holen
print(meinAuto.keys())
print(meinAuto.values())
print(meinAuto.items())

####################################################################

# Konvertierungen
# Typen von Variablen verändern
x = [1, 2, 3, 4]
print(tuple(x))  # list -> tuple
print(tuple(range(10)))  # range -> tuple

zahl = "123"
print(zahl * 2)  # 123123
print(int(zahl) * 2)  # str -> int: 246

k = 123.456  # Kommastellen abschneiden
print(int(k))  # float -> int

b = True
print(int(b))  # bool -> int

i = 10
print(bool(i))  # int -> bool (0: False, nicht 0: True)
print(bool(0))

####################################################################

