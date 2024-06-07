import sqlite3

# connection = sqlite3.connect("Test.db")

class Person:
	def __init__(self, id: int, name: str):
		self.id = id
		self.name = name

	def __str__(self):
		return f"{self.id}, {self.name}"

# Besser
def loadData():
	with sqlite3.connect("Test.db") as connection:
		cursor = connection.cursor()
		# cursor.execute("CREATE TABLE Personen(id int, name varchar(50))")
		# cursor.execute("INSERT INTO Personen VALUES (1, 'Lukas')")
		# cursor.execute("INSERT INTO Personen VALUES (2, 'Alexander')")
		# cursor.execute("INSERT INTO Personen VALUES (3, 'Martin')")
		x = cursor.execute("SELECT * FROM Personen").fetchall()
		personen = list(map(lambda t: Person(t[0], t[1]), x))
		# connection.commit()
		cursor.close()
		return personen

# ORM: SqlAlchemy