from graphics import *
import random
import time

win=GraphWin('cobrinha..', 1300, 700)

win.setBackground(color_rgb(0, 0, 0))

def line(x1,z1,x2,z2):
    lnex= Line(Point(x1,z1), Point(x2,z2))
    lnex.setFill('black')
    lnex.setWidth(4)
    lnex.draw(win)

def cercaH(x):
    for ind in range(0,1300, 5):
        Ch=Point(ind, x)
        Ch.draw(win)
        Ch.setFill('green')
def cercaV(y):
    for ind in range(0,700, 5):
        Cv=Point(y, ind)
        Cv.draw(win)
        Cv.setFill('green')

line(6,0,6,1300)
line(0,6,1300,6)
line(1295,0,1295, 700)
line(0,695,1300,695)


cercaH(5)
cercaH(695)
cercaV(5)
cercaV(1295)

#--------------------------------------------------
#COBRA
#--------------------------------------------------
def check(controle):
    if win.checkKey() == '':
        return True
    else:
        if win.checkKey() != controle:
            return False
def perde():
    if c >= 1295 or c <= 5:
        return True
    elif x >= 1295 or x <= 5:
        return True
    elif y >= 695 or y <= 5:
        return True
    elif v >= 695 or v <= 5:
        return True
    else:
        return False



x = 650
y = 350
c = 660
v = 360


Cb = Rectangle(Point(x, y), Point(c, v))
Cb.setFill('blue')
Cb.setOutline('yellow')
Cb.draw(win)


def ponto():
    if x or y == mx or my:
        return True
    else:
        return False


def randomnumb(inicio,final,passo):
    return random.randrange(inicio,final,passo)

mx = randomnumb(10,1285,10)
my = randomnumb(10,685,10)
Mc = Rectangle(Point(mx, my), Point(mx + 10, my + 10))
Mc.setFill(color_rgb(255, 0, 0))
Mc.setOutline(color_rgb(255, 0, 0))

pts = 0

bateu = False
passo = 5
continuar = True
while continuar:
    tecla = win.checkKey()
    '''
    if ponto() == True:
        pts += 15
        Mc.undraw()
        Mc.draw(win)
    else:
        break
    '''

    if bateu:
        passo = passo - passo
        t = Text(Point(650, 350), "VOCÊ PERDEU")
        t.setOutline("black")
        t.setFill('red')
        t.setSize(35)
        t.draw(win)
        continuar = False
        if win.getMouse():
            bateu = False


    if tecla == 'w':
        w = True
        while w == True:
            bateu = perde()
            if bateu == True:
                break
            Cb.undraw()
            y -= passo
            v -= passo
            Cb = Rectangle(Point(x, y), Point(c, v))
            Cb.setFill('green')
            Cb.setOutline('green')
            Cb.draw(win)
            w = check('w')
            time.sleep(0.2)

    if tecla == 'a':
        a = True
        while a == True:
            bateu = perde()
            if bateu == True:
                break
            Cb.undraw()
            x -= passo
            c -= passo
            Cb = Rectangle(Point(x, y), Point(c, v))
            Cb.setFill('green')
            Cb.setOutline('green')
            Cb.draw(win)
            a = check('a')
            time.sleep(0.2)

    if tecla == 's':
        s = True
        while s == True:
            bateu = perde()
            if bateu == True:
                break
            Cb.undraw()
            y += passo
            v += passo
            Cb = Rectangle(Point(x, y), Point(c, v))
            Cb.setFill('green')
            Cb.setOutline('green')
            Cb.draw(win)
            s = check(s)
            time.sleep(0.2)

    if tecla == 'd':
        d = True
        while d == True:
            bateu = perde()
            if bateu == True:
                break
            Cb.undraw()
            x += passo
            c += passo
            Cb = Rectangle(Point(x, y), Point(c, v))
            Cb.setFill('green')
            Cb.setOutline('green')
            Cb.draw(win)
            d = check('d')
            time.sleep(0.2)

    #print(pts)


