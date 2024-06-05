# Kontrollstrukturen
# Normalerweise läuft das Skript von oben nach unten
# Mit Kontrollstrukturen können wir den Codefluss anpassen

# if-Anweisung
# Benötigt eine oder mehrere Bedingungen
# Wenn die Bedingung(en) auf True wird/werden, wird der Code innerhalb der if-Anweisung ausgeführt

z1 = 3
z2 = 8
if z1 > z2:
	print("z1 ist größer als z2")  # WICHTIG: Einrückungen nicht vergessen
	print("Hallo")  # Diese Anweisung gehört durch die Einrückung auch zur if dazu
print("Außerhalb")  # Diese Anweisung gehört ohne Einrückung NICHT zur if dazu


if z1 > z2:
	print("z1 ist größer als z2")
elif z1 < z2:  # else mit Bedingung (etwas anderes)
	print("z1 ist kleiner als z2")
else:  # else ohne Bedingung (alles andere)
	print("z1 ist gleich z2")


if z1 > z2:
	if z1 > 5:
		print("z1 ist größer als z2 und größer als 5")  # Hier werden zwei Einrückungen benötigt
	print("z1 ist größer als z2")

############################################################################

# Vergleichsoperatoren
# ==, !=, <>
# <, >, <=, >=

# Logische Operatoren
# and, or, not
# &, |, ~
# in, is

if z1 > z2 and z1 > 5:  # Beide Bedingungen müssen True sein
	print("z1 ist größer als z2 UND größer als 5")

if z1 > z2 or z1 > 5:  # Eine von beiden oder beide Bedingungen müssen True sein
	print("z1 ist größer als z2 ODER größer als 5")

# if not z1 > z2:
# if z1 <= z2:

# in: Sucht ein gegebenes Element in einer Liste

# Aufgabenstellungen: Ist z1 1, 3, 5 oder 10?
if z1 == 1 or z1 == 3 or z1 == 5 or z1 == 10:
	print("z1 ist 1, 3, 5 oder 10")

# Alternative: Mit in
if z1 in [1, 3, 5, 10]:
	print("z1 ist 1, 3, 5 oder 10")

# Ist z1 in einer Listenvariable enthalten?
zahlen = [1, 3, 5, 10]
if z1 in zahlen:
	print("z1 ist in der Liste enthalten")

# In invertieren mit not
if z1 not in zahlen:
	print("z1 ist nicht in der Liste enthalten")

# Alternative zu and und or
if z1 == 1 & z1 == 3 & z1 == 5 & z1 == 10:
	print("z1 ist 1, 3, 5 oder 10")

if z1 == 1 | z1 == 3 | z1 == 5 | z1 == 10:
	print("z1 ist 1, 3, 5 oder 10")

if ~(z1 in zahlen):
	print("z1 ist nicht in der Liste enthalten")

############################################################################

# Ternary Operator
# Größere if/elif/else Konstrukte kompakter machen
if z1 > z2:
	print("z1 ist größer als z2")
elif z1 < z2:
	print("z1 ist kleiner als z2")
else:
	print("z1 ist gleich z2")

print("z1 ist größer als z2") if z1 > z2 \
	else print("z1 ist kleiner als z2") if z1 < z2 \
	else print("z1 ist gleich z2")

print("z1 ist größer als z2" if z1 > z2
      else "z1 ist kleiner als z2" if z1 < z2
	  else "z1 ist gleich z2")

############################################################################

list1 = [1, 2, 3, 4, 10]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
laengen = [len(list1), len(list2), len(list3)]
laengen.sort()
laengste = laengen[-1]
if len(list1) == laengste:
	print("list1 ist die längste Liste")
if len(list2) == laengste:
	print("list2 ist die längste Liste")
if len(list3) == laengste:
	print("list3 ist die längste Liste")


oberliste = [list1, list2, list3]
maxL = -1
listen = []
for l in oberliste:
	x = len(l)
	if x > maxL:
		maxL = x
		listen.clear()
	elif x == maxL:
		listen.append(l)
print(listen)


zahl = 12
if zahl:
	print()

gesamt = list1 + list2 + list3
if 3 in gesamt or 7 in gesamt or 10 in gesamt:
	print("...")


gesucht = {3, 7, 10}
inBeidenListen = gesucht.intersection(gesamt)
if len(inBeidenListen) > 0:
	print(inBeidenListen)
else:
	print("Keine der gesuchten Zahlen enthalten")