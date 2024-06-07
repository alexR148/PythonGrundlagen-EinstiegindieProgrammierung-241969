from tkinter import Tk, Button, Label
import M014

window = Tk()

window.wm_title("Mein erstes Fenster")
window.geometry("600x300+2500+300")
window.config(bg="white")  # Wichtige Methode um alle möglichen Dinge bei Komponenten zu verändern

# Aufgabenstellung: Daten aus der DB anzeigen
button = Button(text="Daten laden")
button.place(width=100, height=30, x=250, y=250)
def load():
	data = M014.loadData()
	row = 1
	for p in data:
		idField = Label(text=p.id, borderwidth=1)
		nameField = Label(text=p.name, borderwidth=1)
		idField.place(x=10, y=20 * row, width=50, height=20)
		nameField.place(x=60, y=20 * row, width=100, height=20)
		row += 1
button.config(command=load)


if __name__ == "__main__":
	window.mainloop()