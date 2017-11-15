leveys = int(input("Anna kentän leveys: ")) 
korkeus = int(input("Anna kentän korkeus: "))

if leveys < 1 or korkeus < 1:
	print("Noin pienelle kentälle ei mahdu ainuttakaan pistettä!")
else:
	x = int(input("Anna x-koordinaatti: "))
	y = int(input("Anna y-koordinaatti: "))

	if x == 0 and y == 0 or x == leveys-1 and y == 0 or x == 0 and y == korkeus-1 or x == leveys-1 and y == korkeus-1:
		print("Antamasi piste (x: {}, y: {}) on kentän nurkassa.".format(x, y))
	elif x >= leveys or y >= korkeus or x < 0 or y < 0:
		print("Antamasi piste (x: {}, y: {}) on kentän rajojen ulkopuolella!".format(x, y))
	elif x == leveys-1 or x == 0 or y == korkeus-1 or y == 0:
		print("Antamasi piste (x: {}, y: {}) on kentän laidalla.".format(x, y))
	else:
		print("Antamasi piste (x: {}, y: {}) on kentän keskellä.".format(x, y))