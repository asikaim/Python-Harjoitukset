from turtle import *

def piirra_tiedostosta(tiedosto):
	with open(tiedosto) as lahde:
		for rivi in lahde.readlines():
			vari, kaarimaara, sade, kasvu, paksuus = rivi.split(",")
			vari = vari.strip()
			kaarimaara = int(kaarimaara)
			sade = int(sade)
			kasvu = float(kasvu)
			paksuus = int(paksuus)
			piirra_spiraali(vari, kaarimaara, sade, kasvu, paksuus)

def piirra_spiraali(vari, kaarimaara, sade, kasvu, paksuus=1):
	color(vari)
	pensize(paksuus)
	for i in range(kaarimaara):
		down()
		circle(sade, 90)
		sade += kasvu
	up()
