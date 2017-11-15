def pyyda_syote(pyynto, virhe):
	"""Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua merkkijonoa. 
		Virheellisen syötteen kohdalla käyttäjälle näytetään toisena parametrina annettu virheilmoitus.
		Käyttäjän antama kelvollinen syöte palautetaan kokonaislukuna."""
	while True:
		kokluku = input(pyynto)
		try:
			if kokluku.isdigit:
				return int(kokluku)
		except ValueError:
			print(virhe)


luku = pyyda_syote("Anna kokonaisluku: ", "Et antanut kokonaislukua")
print("Annoit kokonaisluvun {}! Nohevaa toimintaa!".format(luku))
hemulit = pyyda_syote("Montako hemulia mahtuu muumitaloon? ", "Tämä ei ollut kelvollinen hemulien lukumäärä!")
print("Muumitaloon mahtuu {} hemulia".format(hemulit))
