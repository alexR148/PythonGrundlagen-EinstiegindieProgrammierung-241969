# Schleifen

# Führen Code mehrmals aus
# Am Beginn der Schleife wird die Bedingung geprüft, wenn diese True ist, wird die Schleife wiederholt

# while-Schleife
# Hat eine Bedingung und läuft solange, wie die Bedingung True ist
i = 0
while i < 10:  # Ab hier gehen wir im Kreis
	print(i)
	i += 1
# Sobald i 10 erreicht hat, wird die Schleife beendet

print("Nach der Schleife")

a = 0
b = 10
while a < b:
	print(a)
	a += 1

print("Nach der Schleife")

# break
# Beendet die Schleife
# Wird häufig in Kombination mit einer if benutzt

# continue
# Überspringe den Code nach continue, und bewege den Zeiger zum Schleifenkopf zurück
# Wird häufig in Kombination mit einer if benutzt

# Endlosschleife
while True:
	print("Für immer")
	a += 1
	if a % 10 == 0:
		continue  # Wenn a durch 10 teilbar ist, überspringe den Rest der Schleife

	print(a)
	if a > 500:
		break  # Beende die Schleife

print("Nach der Schleife")

####################################################################

# for-Schleife
# Geht im Kreis wie eine While Schleife, aber benötigt immer eine Liste (list, tuple, set, str, ...)
# Innerhalb der Schleife haben wir immer Zugriff auf das derzeitige Element

# Aufgabenstellung: Alle Zahlen in der Liste ausgeben
zahlen = [1, 2, 3, 4, 5]

index = 0  # Beschreibt, bei welcher Zahl wir uns gerade befinden
while index < len(zahlen):  # Diese Schleife soll solange laufen, bis der Index das Ende Liste erreicht hat
	print(zahlen[index])
	index += 1

# Mit einer For-Schleife:
# zahl ist immer das derzeitige Element
for zahl in zahlen:  # "Für jede Zahl in zahlen"
	print(zahl)

# For-Schleife mit Range
# "klassische For-Schleife"
for i in range(10):  # i = 0; i < 10; i++
	print(i)

text = "Hallo Welt"
for zeichen in text:
	print(zeichen)

# else bei Schleife
# Codeblock, welcher ausgeführt wird, wenn die Schleife erfolgreich (ohne break) zu Ende gelaufen ist
# Kann bei while und bei for verwendet werden
for zahl in zahlen:
	print(zahl)
else:
	print("Schleife erfolgreich beendet")

######################################################################

# fstring (Formatted String)
# Code in einen String einbauen
a = 10
# print("Die Zahl ist " + a)  # Nicht möglich, da ein str und ein int nicht addiert werden können
print("Die Zahl ist " + str(a))
print("Die Zahl ist " + a.__str__())

# Mit fstring
print(f"Die Zahl ist {a}")

for i in range(10):
	print("Die Zahl ist: " + str(i))
	print("Die Zahl^2 ist: " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))

	print("-----------------------")

	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl^2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")

# Übung 1:
# FizzBuzz
# 1. Schleife schreiben, die von 1 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1, 2, Fizz, 4, Buzz, ..., 14, FizzBuzz


# Übung 2:
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Der Modulo Operator ist hier sehr nützlich
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden
