# List Comprehension
# Ermöglicht, mithilfe einer Expression innerhalb von Listenklammern schnell eine Liste zu erzeugen
# Kann mit Bedingungen und Wertanpassungen versehen werden

# Aufgabenstellung: Liste mit Zahlen von 1 bis 20

# Mit Schleife
zahlen = []
for i in range(1, 21):
	zahlen.append(i)
print(zahlen)

zahlenLC = [i for i in range(1, 21)]  # Schleife schreiben, an den Anfang springen, i einfügen
print(zahlenLC)

# Aufgabenstellung: Alle Zahlen ausgeben die durch 3 oder 5 teilbar sind
zahlenDurch3oder5 = []
for i in range(1, 100):
	if i % 3 == 0 or i % 5 == 0:
		zahlenDurch3oder5.append(i)
print(zahlenDurch3oder5)

zahlenDurch3oder5LC = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(zahlenDurch3oder5LC)

# Aufgabenstellung: Liste erzeugen von 0 bis 10 mit 0.1 Schritten
zahlen01 = []
for i in range(1, 100):
	zahlen01.append(i / 10)
print(zahlen01)

zahlen01LC = [i / 10 for i in range(1, 100)]
print(zahlen01LC)

# Aufgabenstellung: 1x1
zahlen11 = []
for i in range(1, 11):
	for j in range(1, 11):
		zahlen11.append(f"{i}x{j}={i * j}")
print(zahlen11)

zahlen11LC = [f"{i}x{j}={i * j}" for i in range(1, 11) for j in range(1, 11)]
print(zahlen11LC)

# Aufgabenstellung: FizzBuzz
for i in range(100):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0:
		print("Fizz")
	else:
		print(i)

fizzBuzzLC = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 \
	              else "Buzz" if i % 5 == 0 \
				  else "Fizz" if i % 3 == 0 \
				  else i for i in range(1, 101)]
print(fizzBuzzLC)

# Extra: Tabelle mit LC
for i in range(10):
	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl hoch 2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")

potenzen = [[f"Die Zahl ist: {i}", f"Die Zahl hoch 2 ist: {i ** 2}", f"{i}^2={i ** 2}"] for i in range(1, 11)]
for p in potenzen:
	print(p)

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt, falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
# Verwende hierfür die Split Funktion von String
