import turtle as tr

def franky(dist, frg):
    if frg <= 1:
        tr.forward(dist)
        return
    franky(dist/3, frg-1)
    tr.left(60)
    franky(dist/3, frg-1)
    tr.right(120)
    franky(dist/3, frg-1)
    tr.left(60)
    franky(dist/3, frg-1)
    return

def sheesh(dist, frg):
    for i in range(3):
        franky(dist, frg)
        tr.right(120)

tr.speed(0)

#sheesh(500, 6)

for i in range(8):
    for i in range(50):
        tr.forward(100)
        tr.right(90)
        tr.forward(1)
        tr.right(90)
        tr.forward(100)
        tr.left(90)
        tr.forward(1)
        tr.left(90)
    tr.right(45)
tr.forward(100)
tr.right(90)
tr.forward(50)
for i in range(360):
    tr.forward(3.1419)
    tr.right(1)