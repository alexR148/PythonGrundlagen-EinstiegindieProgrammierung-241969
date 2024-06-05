# Ich bin ein Kommentar
# Mehrzeilige Kommentare existieren nicht

# Variablen
# Name = Wert
x = 5

# WICHTIG: Der Inhalt der Variable ergibt den Typen der Variable

# Typen
# int, str, float, bool

# Ganze Zahl: int
# Int in Python kann beliebig große/kleine Zahlen halten
y = 397493265198123074093215698210473859162956298
print(y)

# Kommazahl: float
# Float in Python kann beliebig große/kleine Zahlen halten
z = -239569712084329816579213.3280912650943279632896518053219743021375941047932147843681942036498365
print(z)

# Text: str
t = "Text"
print(type(t))  # <class 'str'>

t = 'Text'  # Einzelne oder doppelte Hochkomma möglich

# Wahr-/Falsch Wert: bool
# boolsche Werte werden groß geschrieben
b = True
b = False
print(b)

# Komplexe Zahlen: complex
c = 5 + 12j
print(c)

# Stringfunktionen

text = "Hallo ich bin ein Text"
text.upper()
text.lower()

text.isnumeric()
text.isalpha()
text.isalnum()

print(text.split(" "))

text.capitalize()
text.title()

text.strip(" ")
text.lstrip(" ")
text.rstrip(" ")

# Index
print(text)

print(text[3])
print(text[0])

print(text[-1])  # Das letzte Zeichen

print(text[0:3])  # Nimm alle Zeichen von 0 bis 3 (ohne Obergrenze)
print(text[-4:-1])
# print(text[-4:0])
print(text[3:])  # Von Stelle 3 bis zum Ende
print(text[:3])  # Vom Anfang bis zu Stelle 3
print(text[-4:])

print(text[:])  # Alles

# Arithmetik

# +, -, *, /
z1 = 4
z2 = 7

print(z1 + z2)  # Originale Werte werden nicht verändert
z1 += z2  # Hier wird z1 verändert

print(z1 % z2)
z1 %= z2

print(z1, z2)
print(z1 ** z2)  # Potenzierung

print(z2 / z1)  # 1.75
print(z2 // z1)  # 1

z1 **= z2

# Strings verarbeiten mit Arithmetik
t1 = "Hallo"
t2 = "Welt"
print(t1 + t2)

print(t1 * 10)
print(type(t1[0]))  # Einzelne Character sind auch Strings