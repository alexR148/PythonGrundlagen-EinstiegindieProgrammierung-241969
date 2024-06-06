# Funktionen
# Code kann in Funktionen abgelegt werden, damit dieser mehrmals wiederverwendet werden kann

# Funktionen werden mit dem def Keyword definiert

# Aufbau: def <Name>(): ...
def hallo():
	print("Hallo Welt! Mein Name ist Lukas")

# Funktion verwenden mit <Name>()
hallo()
hallo()
hallo()  # Wenn die Funktion verändert wird (oben), wird der Code bei allen drei Aufrufen angepasst

# Funktion mit Parametern
# Eine Funktion kann beliebig viele Parameter haben
# Diese Parameter können in der Funktion verwendet werden
# Beispiel: Funktion, welche den User begrüßt
def hallo(name):
	print(f"Hallo {name}")

hallo("Lukas")
hallo("Alexander")
hallo("Martin")

# Funktionen mit Ergebnis (Rückgabewert)
# Diese Funktion benötigt zwei Parameter
# Beim Aufruf müssen diese Parameter mitgegeben werden
def addiere(x, y):
	return x + y

summe = addiere(8, 3)  # Der Wert der hier bei return herauskommt, kann in eine Variable geschrieben werden
print(summe)

# Beispiel: isnumeric()
def isnumeric(string):
	for zeichen in string:
		if zeichen not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # Prüfe, ob das derzeitige Zeichen keine Zahl von 0 bis 9 ist
			return False  # Wenn das der Fall ist, ist der gesamte String nicht numerisch
	return True  # Wenn jedes Zeichen eine Zahl ist, ist der gesamte String numerisch

print(isnumeric("Hallo"))  # False
print(isnumeric("123"))  # True

##############################################################################

# Problem mit Funktionen in Python
addiere(7, 4)  # Funktioniert
addiere("Hallo", "Welt")  # Funktioniert auch
addiere([1, 2, 3], [4, 5, 6])  # Funktioniert auch
# addiere([1, 2], "Welt")  # TypeError: can only concatenate list (not "str") to list

# Zwei Lösungsansätze

# 1. Lockere Ansatz
# Typempfehlung
def addiere2(x: int, y: int):  # Hier können wir Empfehlungen für den/die erwarteten Typ(en) geben
	return x + y

addiere2(7, 4)
addiere2("Hallo", "Welt")
addiere2([1, 2, 3], [4, 5, 6])
# addiere2([1, 2], "Welt")
# Code wird trotzdem ausgeführt

addiere2(7.4, 8.2)  # Eigentlich in Ordnung

def addiere3(x: int | float, y: int | float):  # Hier können wir Empfehlungen für den/die erwarteten Typ(en) geben
	return x + y

addiere3(4, 5)  # Funktioniert
addiere3(7.4, 8.2)  # Funktioniert auch
addiere3(4, 6.2)  # Jetzt auch Mischungen möglich

# 2. Strenger Ansatz
# Typvergleich
def addiere4(x: int, y: int):
	if type(x) == int and type(y) == int:
		return x + y
	else:
		raise TypeError("x und y müssen vom Typ int sein!")

def addiere5(x: int | float, y: int | float):
	if type(x) in [int, float] and type(y) in [int, float]:
		return x + y
	else:
		raise TypeError("x und y müssen vom Typ int oder float sein!")

addiere5(4, 8)
addiere5(4.8, 2.3)
# addiere5("Hallo", "Welt")  # Absturz

# Rückgabewertempfehlung
def dividiere(x: int, y: int) -> int | float:
	return x / y

dividiere(5, 3)

##############################################################################

# Problem: Überladung ist in Python nicht möglich
def subtrahiere(x, y):
	return x - y

def subtrahiere(x, y, z):  # Hier wird die Funktion darüber gelöscht/überschrieben
	return x - y - z

# subtrahiere(3, 4)  # Hier fehlt z
subtrahiere(3, 4, 5)

# Mithilfe von optionalen Parametern, können gleich benannte Funktionen mit unterschiedlichen vielen Parametern definiert werden
def subtrahiere2(x, y, z = 0):
	return x - y - z

# Hier ist jetzt beides möglich
subtrahiere2(3, 4)
subtrahiere2(3, 4, 5)

# Praxisbeispiel: read_csv aus Pandas
# Hat 30+ optionale Parameter um alle möglichen Fälle abzudecken
# def read_csv(filepath_or_buffer, *, sep=_NoDefault.no_default, delimiter=None, header='infer', names=_NoDefault.no_default, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=_NoDefault.no_default, skip_blank_lines=True, parse_dates=None, infer_datetime_format=_NoDefault.no_default, keep_date_col=_NoDefault.no_default, date_parser=_NoDefault.no_default, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', delim_whitespace=_NoDefault.no_default, low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=_NoDefault.no_default):
# 	...

# Parameter setzen per Keyword mit Gleichheitszeichen
def multipliziere(a = 1, b = 1, c = 1, d = 1, e = 1):
	return a * b * c * d * e

multipliziere(b=5, e=8)  # Jetzt können wir nur die Parameter setzen, die wirklich interessant sind
multipliziere(a=5, d=8)
multipliziere(a=5, e=3, d=8)

##############################################################################

# Arbitrary Arguments
# Parameter, welcher beliebig Werte empfangen kann
# Werden in Dokumentationen als *args bezeichnet
def summiere(*zahlen: int | float):  # Bei dem * Parameter werden die Werte übergeben
	summe = 0
	for zahl in zahlen:
		summe += zahl
	return summe

# Beliebig viele Parameter möglich
summiere(2, 3)
summiere(3, 4, 5, 6, 7)
summiere(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
summiere(1)
summiere()  # Keine Parameter sind auch beliebig viele Parameter

# Arbitrary Keyword Arguments
# Parameter, welcher beliebig BENANNTE Werte empfangen kann
# Werden in Dokumentationen als **kwargs bezeichnet
def printTeilnehmer(**tn: str):  # **tn ist ein dict
	for key, value in tn.items():  # for Schleife mit zwei Laufvariablen
		print(f"{key} heißt {value}")

printTeilnehmer(Trainer="Lukas", TN1="Alexander", TN2="Martin")

##############################################################################

# Unpacking
# Liste in ihre Einzelteile zerlegen mithilfe von dem * und ** Operator
# * wird bei Listentypen (list, tuple, set, ...), ** wird bei dict verwendet

# Aufgabenstellung: Liste in summiere einbauen
zahlen = [3, 1, 8, 2, 8]
# summiere(zahlen)  # Expected type 'int | float', got 'list[int]' instead

summiere(*zahlen)
a, b, c, d, e = zahlen  # Hier werden die Inhalte der Liste auf die einzelnen Variablen aufgeteilt
print(a)
print(b)
print(c)
print(d)
print(e)

tn = {
	"Trainer": "Lukas",
	"TN1": "Alexander",
	"TN2": "Martin"
}

# printTeilnehmer(tn)
printTeilnehmer(**tn)  # Funktioniert

# x, y, *z = zahlen  # Zu viele Werte (3 erwartet, 5 bekommen)
x, y, *z = zahlen  # Mit einem * vor einer Variable, empfängt diese Variable den Rest der nicht mehr hineinpasst
print(x, y, z)

##############################################################################

# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt
def maximum(*zahlen: int):
	# return max(zahlen)
	if len(zahlen) == 0:
		return 0

	m = zahlen[0]
	# m = -sys.maxsize
	for zahl in zahlen:
		if zahl > m:
			m = zahl
	return m

print(maximum(2, 8, 1, 39, 28, 14, 2))
print(maximum(-4, -2, -9, -1))
maximum()

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
def countCase(text: str):
	lower, upper, sonder = 0, 0, 0
	for buchstabe in text:
		if buchstabe.islower():
			lower += 1
		elif buchstabe.isupper():
			upper += 1
		else:
			sonder += 1
	return f"Groß: {upper}, Klein: {lower}, Sonderzeichen: {sonder}"

print(countCase("Hallo Welt 123!"))

# Übung 3
# Schreibe eine Funktion, die eine Liste von Strings als Parameter empfängt
# Diese Funktion soll die Strings als eine Aufzählung zusammenbauen und am Ende zurück geben
# Beispiele:
# Parameter: []
# Keine Parameter angegeben
# Parameter: ["Teilnehmer"]
# Teilnehmer
# Parameter: ["Teilnehmer1", "Teilnehmer2"]
# Teilnehmer1 und Teilnehmer2
# Parameter: ["Teilnehmer1", "Teilnehmer2", "Teilnehmer3", "Teilnehmer4"]
# Teilnehmer1, Teilnehmer2, Teilnehmer3 und Teilnehmer4
def listTeilnehmer(*teilnehmer: str):
	if len(teilnehmer) == 0:
		print("Keine Teilnehmer")
	elif len(teilnehmer) == 1:
		print(teilnehmer[0])
	elif len(teilnehmer) == 2:
		print(f"{teilnehmer[0]} und {teilnehmer[1]}")
	else:
		gesamt = ""
		z = 1
		for tn in teilnehmer:
			if len(teilnehmer) == z:
				gesamt = gesamt.rstrip(", ") + f" und {tn}"
			else:
				gesamt += f"{tn}, "
			z += 1
		print(gesamt)

def listTeilnehmer2(*teilnehmer: str):
	if len(teilnehmer) == 0:
		print("Keine Teilnehmer")
	elif len(teilnehmer) == 1:
		print(teilnehmer[0])
	elif len(teilnehmer) == 2:
		print(f"{teilnehmer[0]} und {teilnehmer[1]}")
	else:
		gesamt = ""
		for i in range(len(teilnehmer) - 1):
			if len(teilnehmer) - 1 == i:
				gesamt += f" und {teilnehmer[i]}"
			else:
				gesamt += f"{teilnehmer[i]}, "
		print(gesamt)

def listTeilnehmer3(*teilnehmer: str):
	if len(teilnehmer) == 0:
		print("Keine Teilnehmer")

	gesamt = ""
	for i in range(len(teilnehmer) - 1):
		if len(teilnehmer) - 1 == i:
			gesamt += " und "
		else:
			gesamt += ", "

		gesamt += teilnehmer[i]
	print(gesamt.rstrip(" und "))

listTeilnehmer()
listTeilnehmer("T1")
listTeilnehmer("T1", "T2")
listTeilnehmer("T1", "T2", "T3", "T4")