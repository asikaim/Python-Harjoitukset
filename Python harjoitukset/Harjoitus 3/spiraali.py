from turtle import *
def piirra_spiraali(vari, kaarimaara, sade, kasvu, paksuus=1):
	color(vari)
	pensize(paksuus)
	for i in range(kaarimaara):
		down()
		circle(sade, 90)
		sade += kasvu
	up()

piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()
