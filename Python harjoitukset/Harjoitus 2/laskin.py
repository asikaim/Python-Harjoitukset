def plus(luku1, luku2):
	tulos = luku1 + luku2
	print("Tulos: ", tulos)

def minus(luku1, luku2):
	tulos = luku1 - luku2
	print("Tulos: ", tulos)

def kerto(luku1, luku2):
	tulos = luku1 * luku2
	print("Tulos: ", tulos)

def jako(luku1, luku2):
	try:
		tulos = luku1 / luku2
		print("Tulos: ", tulos)
	except ZeroDivisionError:
		print("Tällä ohjelmalla ei pääse äärettömyyteen")


operaatio = input("Valitse operaatio (+, -, *, /): ")

if operaatio == "+":
	try:
		luku1 = float(input("Anna luku 1: "))
	except ValueError:
		print("Ei tämä ole mikään luku")
	else:
		try:
			luku2 = float(input("Anna luku 2: "))
		except ValueError:
			print("Ei tämä ole mikään luku")
		else:
			plus(luku1, luku2)
elif operaatio == "-":
	try:
		luku1 = float(input("Anna luku 1: "))
	except ValueError:
		print("Ei tämä ole mikään luku")
	else:
		try:
			luku2 = float(input("Anna luku 2: "))
		except ValueError:
			print("Ei tämä ole mikään luku")
		else:
			minus(luku1, luku2)
elif operaatio == "*":
	try:
		luku1 = float(input("Anna luku 1: "))
	except ValueError:
		print("Ei tämä ole mikään luku")
	else:
		try:
			luku2 = float(input("Anna luku 2: "))
		except ValueError:
			print("Ei tämä ole mikään luku")
		else:
			kerto(luku1, luku2)
elif operaatio == "/":
	try:
		luku1 = float(input("Anna luku 1: "))
	except ValueError:
		print("Ei tämä ole mikään luku")
	else:
		try:
			luku2 = float(input("Anna luku 2: "))
		except ValueError:
			print("Ei tämä ole mikään luku")
		else:
			jako(luku1, luku2)
else:
	print("Operaatiota ei ole olemassa")