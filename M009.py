# Klassen und Objekte

# int: Ganze Zahl
# float: Kommazahl
# string: Text
# Person: ?

# Klasse
# Komplexe Darstellung von einem Zustand/Sache
# Klasse ist der Bauplan des Objekts
# Aus einer Klasse können beliebig viele Objekte erzeugt werden
# Innerhalb einer Klasse wird der Aufbau der Objekte definiert (Variablen, Funktionen)

# Beispiel Person
# Felder:
# Vorname: str
# Nachname: str
# Alter: int
# Adresse: str
# ...

# Funktionen:
# Sprechen(text)
# Bewegen(distanz)
# ...

# Person Klasse
class Person:
	# __init__
	# Legt den Startzustand des Objekts fest
	# Wird bei Erstellung des Objekts ausgeführt
	# Hier werden die Felder erzeugt und Initialwerte verarbeitet
	def __init__(self, vorname = "", nachname = "", alter = 0, adresse = ""):  # Jede Funktion hat immer self, self: Das Objekt selbst
		self.vorname = ""
		self.nachname = ""
		self.alter = 0
		self.adresse = ""

	# Jetzt kann jede Person sprechen
	# Sprechen bezieht sich hierbei auf das entsprechende Person Objekt
	def sprechen(self, text: str):
		print(f"{self.vorname} {self.nachname} sagt: {text}")

	def bewegen(self, distanz: int):
		print(f"{self.vorname} {self.nachname} bewegt sich um {distanz}m")

# Objekte einer Klasse erstellen
p1 = Person()  # Hier wird __init__ ausgeführt
p1.vorname = "Lukas"  # Durch das anlegen der Felder in __init__ können diese nun beschrieben werden

p2 = Person("Lukas", "Kern", 25, "Zuhause")
# Person.sprechen(p2, "")  # Nicht sinnvoll
p2.sprechen("Hallo")

###################################################################################

# Praktisches Beispiel:

# Schlecht (String Liste):
customer1 = ["ALFKI", "Alfreds Futterkiste", "Maria Anders", "Sales Representative", "Obere Str. 57 Berlin 12209 Germany", "030-0074321"]

# Besser (Model Klasse):
class Customer:
	def __init__(self, CustomerID, CompanyName, ContactName, Title, Address, Phone):
		self.CustomerID = CustomerID
		self.CompanyName = CompanyName
		self.ContactName = ContactName
		self.Title = Title
		self.Address = Address
		self.Phone = Phone

# Objekte von den Daten erstellen
# Normalerweise würden diese Daten hier unten aus der Datenbank geladen werden
customer1Class = Customer("ALFKI", "Alfreds Futterkiste", "Maria Anders", "Sales Representative", "Obere Str. 57 Berlin 12209 Germany", "030-0074321")
print(customer1Class.Phone)

###################################################################################

# Methoden die mit __ beginnen und enden
# Es gibt Methoden die in jeder Klasse standardmäßig existieren
# Diese Methoden werden alle von Object weitergegeben
# Diese Methoden können überschrieben werden z.B. init
class Test:
	def __init__(self):
		print("Hallo Test")

	# Verändert die Standardausgabe von <__main__.Test object at 0x00000268352DBB90> zu einer eigenen Ausgabe
	def __str__(self):
		return "Test"

	# def __add__(self, other):
	# 	pass

test = Test()
test.__str__()  # Macht aus dem test Objekt eine Stringrepräsentation
print(test.__str__())  # <__main__.Test object at 0x00000268352DBB90>
print(test)  # <__main__.Test object at 0x00000268352DBB90>
print([1, 2, 3])  # [1, 2, 3]
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3]
# test += 1

###################################################################################

# docstring
# Beschreiben von Klassen/Funktionen/Variablen/...
class Order:
	'''
	Die Bestellungsklasse welche die entsprechende Datenbank repräsentiert

	Felder:
	OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ...
	'''
	def __init__(self, id):
		"""
		Erstellt ein Bestellungsobjekt mit einer ID

		:param id: Die Eindeutige Nummer dieser Bestellung
		"""
		pass  # Macht nichts (Platzhalter)

	def rechnungssumme(self):
		"""
		Berechnet die Summe aller Artikel innerhalb dieser Rechnung und gibt diese auf zwei Kommastellen gerundet zurück

		:return: Die Summe der Rechnung in Euro
		"""
		pass

###################################################################################

# Neue Felder zu Objekten hinzufügen ohne die Klasse zu verändern
p3 = Person()
p3.wasAuchImmer = "Was auch immer"
print(p3.wasAuchImmer)

del p3.wasAuchImmer

###################################################################################

# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten: (in __init__)
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen (Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum) -> Parameter int (Wieviel soll beschleunigt werden)
#     - StarteMotor (Setze Motorzustand auf True, funktioniert nur wenn das Auto noch nicht gestartet ist)
#     - StoppeMotor (Motor kann nur gestoppt werden, wenn das Auto nicht fährt)
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion (Konkrete Werte)
