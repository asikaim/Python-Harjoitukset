def pyyda_maalit():
	"""Pyytää käyttäjältä ottelun lopputuloksen ja palauttaa syötetyn tuloksen kokonaislukuina."""
	while True:
		tulos = input("Anna ottelun lopputulos: ")
		tulos = tulos.split("-")
		if len(tulos) != 2:
			print("Anna tulos muodossa <maalit 1>-<maalit 2>!")
		else:
			try:
				m1, m2 = int(tulos[0]), int(tulos[1])
				erotus = m1 - m2
				print("Joukkueiden välinen maaliero on ", erotus)			
				return m1, m2
			except ValueError:
				print("Anna tulos muodossa <maalit 1>-<maalit 2>!")

pyyda_maalit()