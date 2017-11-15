PI = 3.1416

def laske_sektorin_ala(sade, kulma):
	return kulma / 360 * PI * sade ** 2

print(round(laske_sektorin_ala(13.742, 68), 4))