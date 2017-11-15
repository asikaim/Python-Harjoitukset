def pyyda_syote(pyynto, virhe):
	"""Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua merkkijonoa.
	Virheellisen syötteen kohdalla käyttäjälle näytetään toisena parametrina annettu virheilmoitus.
	Käyttäjän antama kelvollinen syöte palautetaan kokonaislukuna.
	Hyväksyy vain luvut jotka ovat suurempia kuin 1."""
	while True:
		kokluku = input(pyynto)
		try:
			if kokluku.isdigit:
				kokluku = int(kokluku)
				if kokluku > 1:
					return kokluku
				else:
					print(virhe)
		except ValueError:
			print(virhe)

def tarkista_alkuluku(luku):
	"""Tarkistaa onko parametrina annettu luku alkuluku.
	Palauttaa False jos luku ei ole alkuluku; jos luku on alkuluku palautetaan True"""
	for x in range(2, int(luku**0.5)+1):
		if luku % x == 0:
			return False
	return True

luku = pyyda_syote("Anna kokonaisluku, joka on suurempi kuin 1: ", "Pieleen meni :'(")
if tarkista_alkuluku(luku) is True:
	print("Kyseessä on alkuluku")
else:
	print("Kyseessä ei ole alkuluku")
