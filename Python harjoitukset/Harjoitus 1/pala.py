from math import sqrt
PI = 3.1416

def laske_nelion_ala(sivu):
	neliopala = sivu * sivu
	return neliopala

def laske_ympyran_ala(r):
	return PI * r ** 2

def laske_sektorin_ala(sade, kulma):
	return kulma / 360 * PI * sade ** 2

def laske_kolmion_ala(pituus):
	return pituus * pituus / 2

def laske_sivun_pituus(hypo):
    return sqrt((hypo ** 2) / 2)

def laske_kuvion_ala(x):
	nelio1 = laske_nelion_ala(x)
	sade1 = laske_sivun_pituus(x)
	kolmio1 = laske_kolmion_ala(sade1)
	halkaisija1 = sade1 * 2
	sektori1 = laske_sektorin_ala(sade1, 45)
	ympyra1 = laske_ympyran_ala(sade1)
	nelio2 = laske_nelion_ala(halkaisija1)
	sade2 = halkaisija1
	sektori2 = laske_sektorin_ala(sade2, 90)
	ympyra2 = laske_ympyran_ala(sade2)

	return nelio1 + kolmio1 + sektori1 + nelio2 + ympyra2 - sektori2

print(round(laske_kuvion_ala(3.467), 4))