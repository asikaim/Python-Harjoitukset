import haravasto
tila = {
	"planeetta": None
}

def tulvataytto(planeetta, x, y):
	"""Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että täyttö aloitetaan annetusta x, y -pisteestä."""
	pino = [(x, y)]
	leveys = len(planeetta[0])
	korkeus = len(planeetta)
	if planeetta[y][x] == "x":
		pass
	else:
		while pino:
			x, y = pino.pop()
			if planeetta[y][x] == " ":
				planeetta[y][x] = "0"
			for nx in range(min(max(x-1, 0), leveys), min(max(x+2, 0), leveys)):
				for ny in range(min(max(y-1, 0), korkeus), min(max(y+2, 0), korkeus)):
					if planeetta[ny][nx] == " ":
						pino.append((nx, ny))


def piirra_kentta():
	"""Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän ruudut näkyviin peli-ikkunaan.
	Funktiota kutsutaan aina kun pelimoottori pyytää ruudun näkymän päivitystä."""
	planeetta = tila["planeetta"]
	haravasto.piirra_tausta()
	haravasto.aloita_ruutujen_piirto()
	for x in range(len(planeetta[0])):
		for y in range(len(planeetta)):
			if planeetta[y][x] == "x":
				haravasto.lisaa_piirrettava_ruutu("x", x * 40, y * 40)
			else:
				haravasto.lisaa_piirrettava_ruutu(" ", x * 40, y * 40)
	haravasto.piirra_ruudut()

def main():
	"""Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän."""
	haravasto.lataa_kuvat("spritet")
	haravasto.luo_ikkuna(len(planeetta[0] * 40), len(planeetta * 40))
	haravasto.aseta_piirto_kasittelija(piirra_kentta)
	haravasto.aloita()

if __name__ == "__main__":
	planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "], 
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "], 
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "], 
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
	]
	tila["planeetta"] = planeetta
	tulvataytto(planeetta, 7, 2)
	main()
