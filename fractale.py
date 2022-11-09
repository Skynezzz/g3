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

for i in range(12):
    for i in range(25):
        tr.forward(50)
        tr.right(90)
        tr.forward(1)
        tr.right(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(1)
        tr.left(90)
    tr.right(30)
tr.forward(50)
tr.right(90)
tr.forward(24)
for i in range(360):
    tr.forward(2.51)
    tr.right(1)