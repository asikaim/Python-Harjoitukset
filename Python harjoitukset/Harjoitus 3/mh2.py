def tarkista_koordinaatit(x, y, leveys, korkeus):
	"""Tarkistaa ovatko annetut x, y -koordinaatit annettujen rajojen sisällä. Palauttaa True, jos koordinaatit ovat rajojen sisällä; muuten palautetaan False."""
	if x >= leveys or y >= korkeus or x < 0 or y < 0:
		return False
	else:
		return True

def kysy_koordinaatit(leveys, korkeus):
	"""Pyytää käyttäjältä koordinaatteja kunnes käyttäjä antaa kaksi kokonaislukua, joista molemmat ovat annetun kentän rajojen sisäpuolella, tai tyhjän syötteen. Palauttaa saadut koordinaatit. Jos käyttäjä antaa tyhjän syötteen, palautetaan kaksi None-arvoa."""
	while True:
		koordinaatit = input("Anna koordinaatit tai lopeta tyhjällä: ")

		if koordinaatit == "":
			koordX = None
			koordY = None
			return koordX, koordY

		koordinaatit = koordinaatit.split(" ")
 
		if len(koordinaatit) != 2:
			print("Anna kaksi koordinaattia välilyönnillä erotettuna")
		else:
			try:
				koordX, koordY = int(koordinaatit[0]), int(koordinaatit[1])
				if tarkista_koordinaatit(koordX, koordY, leveys, korkeus) is False:
					print("Koordinaatit ovat ruudukon ulkopuolella")
				else:
					return koordX, koordY
			except ValueError:
				print("Anna koordinaatit kokonaislukuina")

def avaa_ruutuja(kentta):
	"""Avaa pelikentällä olevia ruutuja merkitsemällä ne x:llä. Avattavia ruutuja kysytään käyttäjältä kunnes tämä haluaa lopettaa antamalla tyhjän syötteen. Kentän tila tulostetaan jokaisen avauksen jälkeen."""
	leveys = len(kentta[0])
	korkeus = len(kentta)
	while True:
		raksi = kysy_koordinaatit(leveys, korkeus)
		if raksi[0] == None and raksi[1] == None:
			break
		for i in range(leveys):
			for j in range(korkeus):
				kentta[raksi[1]][raksi[0]] = "x"
		print(*kentta, sep='\n')

kentta = [['o','o','o','o','o','o'], ['o','o','o','o','o','o'], ['o','o','o','o','o','o'], ['o','o','o','o','o','o']]
avaa_ruutuja(kentta)