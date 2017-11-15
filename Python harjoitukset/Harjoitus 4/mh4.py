import haravasto as har

def hiiri_kasittelija(x, y, nappi, muokkausnapit):
	"""Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
	Tulostaa hiiren sijainnin sekä painetun napin terminaaliin."""
	napit = {har.HIIRI_VASEN: "vasen",
			har.HIIRI_KESKI: "keski",
			har.HIIRI_OIKEA: "oikea"}

	print("Hiiren nappia {} painettiin kohdassa {},{}.".format(napit[nappi], x, y))

def main():
	"""Luo sovellusikkunan ja asettaa käsittelijäfunktion hiiren klikkauksille. 
	Käynnistää sovelluksen."""
	har.luo_ikkuna()
	har.aseta_hiiri_kasittelija(hiiri_kasittelija)
	har.aloita()

if __name__ == "__main__":
    main()