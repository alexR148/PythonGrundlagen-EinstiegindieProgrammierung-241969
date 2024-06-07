# Lambda
# Funktionen, welche keinen Namen haben
# Nur einmal verwenden
# -> anonyme Funktionen
def hallo():
	print("Hallo")

f = hallo  # Funktionszeiger auf hallo

print(f)  # <function hallo at 0x000001B24BC0A2A0>

f()  # Funktionszeiger ausführen

# Anonyme Variante
f2 = lambda: print("Hallo")

print(f2)  # <function <lambda> at 0x000001DB72077740>

f2()  # Funktionszeiger ausführen

###########################################################

# Verwendung von Lambda-Expressions

# filter, map

# filter: Durchsucht eine Liste nach einem Kriterium
# Das Kriterium ist eine Lambda-Expression

bis100 = list(range(100))

# Aufgabenstellung: Alle Zahlen filtern, welche durch 2 teilbar sind
filterung = filter(lambda item: item % 2 == 0, bis100)  # Hier wird eine Funktion benötigt, welche einen Parameter hat, und bool zurückgibt
# filter macht eine Schleife über die Liste, und gibt jedes Element zurück, bei dem die gegebenene Bedingung True zurückgibt

# Normale Schleife
ergebnis = []
for item in bis100:
	if item % 2 == 0:
		ergebnis.append(item)

print(ergebnis)
print(filterung)  # <filter object at 0x000001B819F857B0>: Filter Generator
print(list(filterung))

# filter mit einer normalen Methode (def)
def durch2(item: int):
	return item % 2 == 0
filter(durch2, bis100)

filterungLC = [item for item in bis100 if item % 2 == 0]
print(filterungLC)

###########################################################

# map

# Wandelt jedes Element der Liste in eine neue Form um

# Aufgabenstellung: Jedes Element einer Liste (bis100) durch 5 teilen
mapping = map(lambda item: item / 5, bis100)

# Normale Schleife
ergebnis2 = []
for item in bis100:
	ergebnis2.append(item / 5)

print(ergebnis2)
print(mapping)  # <map object at 0x0000023E93975F60>: Map Generator
print(list(mapping))

# map mit einer normalen Methode (def)
def durch5(item: int):
	return item / 5
map(durch5, bis100)

mappingLC = [item / 5 for item in bis100]
print(mappingLC)

###########################################################

# Aufgabenstellung: Eigene Funktion, welche eine Lambda-Expression empfängt, und die Elemente zählt, welche der Lambda-Expression entsprechen
def count(iterable, l):
	output = 0
	for x in iterable:
		if l(x) == True:  # Führe bei jedem Schleifendurchlauf die Lambda-Expression aus
			output += 1
	return output

print(count(bis100, lambda x: x % 5 == 0))  # 20