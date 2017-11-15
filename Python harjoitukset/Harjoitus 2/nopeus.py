def nopeuslaskuri(matka, aika):
	nopeus = (matka / 1000) / (aika / 3600)
	print("{:.2f} metriä {:.2f} sekunnissa kulkeneen auton nopeus on {:.2f} km/h.".format(matka, aika, nopeus))

matka = float(input("Anna auton kulkema matka (m): "))
aika = float(input("Anna matkaan kulunut aika (s): "))
nopeuslaskuri(matka, aika)