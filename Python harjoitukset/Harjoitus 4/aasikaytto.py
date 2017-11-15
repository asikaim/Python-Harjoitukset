import aasimaaritelmat as am
def nayta_tila(aasidata):
	"""Tulostaa aasin tilan."""
	print("Aasi on {} vuotta vanha ja rahaa on {} mk".format(aasidata["IKÄ"], aasidata["RAHA"]))
	print("Kylläisyys: {}".format(aasidata["KYLLÄISYYS"]))
	print("Onnellisuus: {}".format(aasidata["ONNELLISUUS"]))
	print("Jaksaminen: {}".format(aasidata["JAKSAMINEN"]))
	if aasidata["ELÄKE"] == True:
		print("Aasi on jäänyt eläkkeelle.")

def pyyda_syote(aasidata):
	"""Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja kysyy uutta syötettä kunnes käyttäjä antaa laillisen syötteen. Saatu syöte palautetaan."""
	if aasidata["ELÄKE"] == True:
		print("Eläkevalinnat: {}, {}".format(am.LOPETA, am.ALUSTA))
	else:
		print("Valinnat: {}, {}, {}, {}".format(am.LOPETA, am.RUOKI, am.KUTITA, am.TYOSKENTELE))
	while True:
		if aasidata["ELÄKE"] == True:
			syote = input("Anna seuraava valinta: ")
			if syote in am.ELAKEVALINNAT:
				return syote
			else:
				print("Virheellinen syöte!")
		else:
			syote = input("Anna seuraava valinta: ")
			if syote in am.VALINNAT:
				return syote
			else:
				print("Virheellinen syöte!")
