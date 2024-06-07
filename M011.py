# Fehlerbehandlung
# Manchmal treten Fehler im Programm auf, welche das Programm abstürzen lassen

# eingabe = input("Gib eine Zahl ein: ")
# zahl = int(eingabe)
# print("Nach dem Input")  # Wird nicht ausgeführt, wenn der Benutzer keine Zahl eingibt

# try-except
# try-Block: Enthält den Code, welcher abstürzen könnte
# except-Block: Enthält den Fehlerbehandlungscode, falls ein Fehler auftritt
try:
	eingabe = input("Gib eine Zahl ein: ")
	zahl = int(eingabe)
	print(10 / zahl)  # Wenn der User eine 0 eingibt, wird hier ein Fehler auftreten
except ValueError:  # Hier kommt der Code hinein, falls der User keine Zahl eingegeben hat
	print("Bitte gib eine Zahl ein.")
except ZeroDivisionError as e:  # Mit as <Name> kann ein Fehler einen Namen bekommen, um auf detailierte Information zugreifen zu können
	print("Division durch 0 ist nicht erlaubt")

	# Hier können innerhalb von e bestimmte Information für den Entwickler herausgegriffen werden
	import traceback
	with open("Log.txt", "a") as f:
		f.writelines(traceback.format_exception(e))
except:  # Alle anderen Fehler fangen
# except Exception as e:  # Alle anderen Fehler fangen
	print("Anderer Fehler")
else:
	print("Wird ausgeführt, wenn kein Fehler auftritt")
finally:
	print("Wird immer ausgeführt, egal ob ein Fehler auftritt oder nicht")

print("Nach dem Input")

# raise
# Selbst Fehler verursachen (Absturz verursachen)
# Wird in Codebasen verwendet, die von anderen Entwicklern weiterverwendet werden
raise RuntimeError("Das hier ist ein Fehler")

class TestException(Exception):
	pass

try:
	raise TestException
except TestException:
	print("TestException verursacht")

# Übung 1
# Erstelle ein Programm, das den User nach zwei Integern fragt
# Falls der User zwei Integer eingibt sollen diese addiert und das Ergebnis in der Konsole ausgegeben werden und das Programm kann beendet werden
# Falls der Benutzer einen falschen Typen eingibt soll das Programm ihn darauf hinweisen, das nur Integer akzeptiert werden und ihn erneut nach den Zahlen fragen

# Übung 2
# Definiere eine beliebige Liste
# Erstelle ein Programm, das den User fragt, das wievielte Element in der Konsole ausgegeben werden soll
# Falls die Zahl außerhalb des Listen-Indexes liegt soll ein Fehler geworfen und der User darauf hingewiesen werden

# Übung 3
# Füge der beschleunigen Funktion deiner Fahrzeug-Klasse aus Modul 9 eine eigene Exception hinzu:
#    - Sie soll geworfen werden, falls die Höchstgeschwindigkeit überschritten wird

# Übung 4
# Erweitere den Rechner aus Übung 7:
# Erstelle eine Klasse namens Rechner und füge dieser zwei Methoden hinzu: Berechne und InputLesen
# Die Berechne Methode soll drei Parameter empfangen (Zahl 1, Zahl 2, Rechenart) und die Berechnung ausführen
# Die InputLesen Methode soll in einer Endlosschleife vom Benutzer Werte einlesen, bis dieser eine Zahl eingegeben hat
# Prüfe bei dieser Methode mittels try-except, ob die Eingabe des Benutzers valide ist (Exception bei der int(...) Methode abfangen)
# Verwende danach drei mal die InputLesen Methode um die Werte zu erhalten und im Anschluss die Berechne Methode um die Berechnung mit den Werten durchzuführen