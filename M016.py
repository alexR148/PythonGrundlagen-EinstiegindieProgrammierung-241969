# Testing
# Sollten regelmäßig ausgeführt werden
# Bei Änderungen im Code kann somit festgestellt werden ob sich in dem letzten Zeitraum Fehler in das Programm eingeschlichen haben

import unittest

class Rechner:
	def addiere(self, a, b):
		return a + b

	def subtrahiere(self, a, b):
		return a - b

class RechnerTests(unittest.TestCase):
	def testeAddiere(self):
		rechner = Rechner()
		summe = rechner.addiere(4, 6)  # Sollte 10 sein
		self.assertEqual(10, summe)

	def testeSubtrahiere(self):
		rechner = Rechner()
		diff = rechner.subtrahiere(4, 6)  # Sollte -2 sein
		self.assertEqual(-2, diff)


if __name__ == "__main__":
	unittest.main()