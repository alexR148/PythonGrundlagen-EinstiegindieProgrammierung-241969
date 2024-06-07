# Decorator
# Beliebige Funktionen mit Code ausstatten, welcher davor oder danach ausgeführt wird

# function-Parameter enthält die zu dekorierende Funktion
def testDecorator(function):
	def wrapper():
		print("Vor der Funktion")
		function()  # Hier wird die originale Funktion einfach ausgeführt, wobei darüber/darunter weiterer Code ausgeführt werden kann
		print("Nach der Funktion")
	return wrapper

@testDecorator
def hallo():
	print("Hallo")

hallo()  # Hier wird jetzt Vor der Funktion und Nach der Funktion ausgegeben

# Decorator mit Parameter
# Wenn eine Funktion Parameter empfängt, müssen diese auch im Decorator mitgegeben werden

def paramDecorator(function):
	def wrapper(*args, **kwargs):
		print("Vor der Funktion")
		function(*args, **kwargs)
		print("Nach der Funktion")
	return wrapper

@paramDecorator
def hallo(text: str):
	print(f"Hallo {text}")

hallo("Welt")

# Sinnvollen Decorator
# Zeitmesser/Stopuhr
import time

def measureTime(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print(f"Dauer: {int((end - start) * 100) / 100}s")
	return wrapper

@measureTime
def generateNumbers(maximum: int):
	list(range(maximum))
# generateNumbers(100_000_000)

########################################################

# @property
# Design-Pattern aus anderen Sprachen, welches über Umwege public/private

class Quadrat:
	def __init__(self, a):
		self._a = a

	@property
	def area(self):
		return self._a ** 2

	@area.setter
	def area(self, newArea: int):
		self._a = newArea ** 0.5

q = Quadrat(5)
print(q.area)

q.area = 10
print(q._a)  # Felder mit _ werden als "private" gekennzeichnet
q._a = 20