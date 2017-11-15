def vaihda_merkit(rivi):
	rivi = rivi.replace('1', '3')
	rivi = rivi.replace('2', '1')
	rivi = rivi.replace('3', '2')
	return rivi

rivi = input("Anna rivi: ")
print(vaihda_merkit(rivi))