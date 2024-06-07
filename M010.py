# Vererbung
# Ermöglicht, Oberklassen zu definieren, welche ihre Variablen und Funktionen nach unten weitervererben
# Unterklassen haben Zugriff auf die vererbten Variablen/Funktionen

# Beispiel:
# Oberklasse: Lebewesen
# Unterklassen: Mensch, Hund, Katze, ...

# In Lebewesen werden verschiedene Variablen/Funktionen definiert, diese werden nach unten vererbt
# Variablen: Bezeichnung, Name
# Funktion: Bewegen

class Lebewesen:
	def __init__(self, bezeichnung: str, name: str):
		self.bezeichnung = bezeichnung
		self.name = name

	def bewegen(self, distanz):
		print(f"{type(self).__name__} hat sich um {distanz}m bewegt")

lebewesen = Lebewesen("Test", "Max")
lebewesen.bewegen(10)
print(lebewesen.name)
print(lebewesen.bezeichnung)

# Innerhalb der Klammer kann eine Oberklasse angegeben werden
# Mensch hat bezeichnung, name und bewegen geerbt
# Mensch kann jetzt Anpassungen bekommen, welche spezifisch zu Mensch sind
# Mensch bekommt jetzt zusätzlich sprache und sprechen
class Mensch(Lebewesen):
	def __init__(self, bezeichnung: str, name: str, sprache: str):
		# super(): Greife in die Oberklasse und führe Code von dort aus
		super().__init__(bezeichnung, name)  # Diese Zeile führt den Code aus der Oberklasse aus

		# Diese beiden Anweisungen werden durch super().__init__ ausgeführt
		##################################
		# self.bezeichnung = bezeichnung #
		# self.name = name               #
		##################################

		self.sprache = sprache

	def sprechen(self, text: str):
		if self.sprache == "DE":
			print(f"{self.name} sagt: {text}")
		if self.sprache == "EN":
			print(f"{self.name} says: {text}")
		# ...

	# Funktionen überschreiben
	# Die Basisklasse (Lebewesen) hat einen Implementation
	# In Mensch können wir jetzt eine spezifische Implementation definieren, welche sich von Lebewesen unterscheidet
	def bewegen(self, distanz):
		print(f"Der Mensch geht {distanz}m")


# Mensch hat jetzt alle Felder/Funktionen aus Lebewesen geerbt
mensch = Mensch("Test", "Max", "DE")
mensch.bewegen(10)
print(mensch.name)
print(mensch.bezeichnung)
mensch.sprechen("Hallo")

class Hund(Lebewesen):
	def __init__(self, bezeichnung, name, fellfarbe):
		super().__init__(bezeichnung, name)
		self.fellfarbe = fellfarbe

	def bewegen(self, distanz):
		print(f"Der Hund läuft {distanz}m")


#####################################################

# Die object Klasse
# object ist die Oberklasse von allen Klassen in Python
# Diese Klasse gibt verschiedene Methoden weiter:
# __init__
# __str__
# ...

print()  # Verlangt einen object Parameter (*values: object)
# Jeder Funktionsparameter, der keine Typempfehlung hat, hat den Typ object
# Jede Klasse, die keine Oberklasse hat, hat auch die object Oberklasse