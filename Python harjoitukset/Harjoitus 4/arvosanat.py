import sys

def kysele_arvosanat():
	"""Pyytää käyttäjältä arvosanoja kunnes käyttäjä antaa nimeksi q. Palauttaa arvosanat listassa, joka sisältää (nimi, arvosana)-monikkoja"""
	arvosanat = []
	while True:
		nimi = input("Anna opiskelijan nimi tai lopeta painamalla q: ")
		if nimi == "q":
			return arvosanat
		else:
			try:
				arvosana = int(input("Anna opiskelijan arvosana: "))
				arvosanat.append((nimi, arvosana))
			except ValueError:
				print("Virhe: arvosanan on oltava kokonaisluku!")

def kirjoita_tiedostoon(tiedosto, arvosanat):
	"""Kirjoittaa arvostelulistan sisällön (opiskelijoiden nimet ja arvosanat) tiedostoon."""
	with open(tiedosto, "w") as kohde:
		for nimi, arvosana in arvosanat:
			kohde.write("{}: {}\n".format(nimi, arvosana))
	print("Kirjoitettiin arvosanat tiedostoon {}".format(sys.argv[1]))

if __name__ == "__main__":
	try:
		arg1 = sys.argv[1]
	except IndexError:
		print("Virhe: kohdetiedoston nimi on annettava komentoriviargumenttina!")
		sys.exit(1)
	arvosanat = kysele_arvosanat()
	kirjoita_tiedostoon(sys.argv[1], arvosanat)