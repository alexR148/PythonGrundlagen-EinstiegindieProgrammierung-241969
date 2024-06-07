class Rechner():
	def berechne(self, z1: int, z2: int, operation: int):
		match operation:
			case 1:
				print(f"{z1} + {z2} = {z1 + z2}")
			case 2:
				print(f"{z1} - {z2} = {z1 - z2}")
			case 3:
				print(f"{z1} * {z2} = {z1 * z2}")
			case 4:
				print(f"{z1} / {z2} = {z1 / z2}")

	def inputLesen(self, text: str):
		while True:
			try:
				zahl = int(input(text))
				return zahl
			except:
				print("Deine Eingabe ist nicht numerisch")


rechner = Rechner()
while True:
	z1 = rechner.inputLesen("Gib eine Zahl ein: ")
	z2 = rechner.inputLesen("Gib eine weitere Zahl ein: ")
	art = 0
	while art not in [1, 2, 3, 4]:
		art = rechner.inputLesen("1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division\nGib eine Rechenoperation ein: ")
	rechner.berechne(z1, z2, art)

	w = input("Neue Berechnung? (Y)")
	if w.lower() != "y":
		break