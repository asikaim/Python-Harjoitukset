from turtle import *

def piirra_nelio(pituus, x, y):
    up()
    setx(x)
    sety(y)

    if x < 0:
        color("red")
    elif x > 0:
        color("blue")

    down()
    begin_fill()
    forward(pituus)
    left(90)
    forward(pituus)
    left(90)
    forward(pituus)
    left(90)
    forward(pituus)
    end_fill()


piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
done()
