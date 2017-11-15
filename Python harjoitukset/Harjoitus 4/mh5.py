import haravasto
from random import randint

tila = {
    "kentta": None
}

def miinoita(kentta, jaljella, maara):
	"""Asettaa kentällä N kpl miinoja satunnaisiin paikkoihin."""
	miinat = 0
	while miinat < maara:
		x = randint(0, len(kentta)-1)
		y = randint(0, len(kentta[0])-1)
		if kentta[x][y] == " ":
			kentta[x][y] = "x"
			miinat += 1

def piirra_kentta():
	"""Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän ruudut näkyviin peli-ikkunaan.
	Funktiota kutsutaan aina kun pelimoottori pyytää ruudun näkymän päivitystä."""
	kentta = tila["kentta"]
	haravasto.tyhjaa_ikkuna()
	haravasto.piirra_tausta()
	haravasto.aloita_ruutujen_piirto()
	for x in range(len(kentta[0])):
		for y in range(len(kentta)):
			if kentta[y][x] == "x":
				haravasto.lisaa_piirrettava_ruutu("x", x * 40, y * 40)
			else:
				haravasto.lisaa_piirrettava_ruutu(" ", x * 40, y * 40)
	haravasto.piirra_ruudut()

def main():
	haravasto.lataa_kuvat("spritet")
	haravasto.luo_ikkuna(400, 400)
	haravasto.aseta_piirto_kasittelija(piirra_kentta)
	haravasto.aloita()

if __name__ == "__main__":
	kentta = []
	for rivi in range(10):
		kentta.append([])
		for sarake in range(10):
			kentta[-1].append(" ")

	tila["kentta"] = kentta

	jaljella = []
	for x in range(10):
		for y in range(10):
			jaljella.append((x, y))

	miinoita(kentta, jaljella, 25)
	main()