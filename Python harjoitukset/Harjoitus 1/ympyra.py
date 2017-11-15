from turtle import *

def piirra_ympyra(x, y, r):
	up()
	setx(x)
	sety(y - r)
	down()
	circle(r)


piirra_ympyra(50, 50, 30)
up()
setx(50)
sety(50)
done()

