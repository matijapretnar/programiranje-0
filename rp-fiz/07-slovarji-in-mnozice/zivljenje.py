import math
import time
from risanje import risba, v_okvirju


def korak(zive):
    sosedje = {}
    for x, y in zive:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (dx, dy) != (0, 0):
                    celica = (x + dx, y + dy)
                    sosedje[celica] = sosedje.get(celica, 0) + 1
    return {celica for celica, n in sosedje.items()
            if n == 3 or n == 2 and celica in zive}


def preberi(vzorec):
    return {(x, -y)
            for y, vrstica in enumerate(vzorec.split('\n'))
            for x, znak in enumerate(vrstica)
            if znak == '#'}


def narisi(zive, x0, y0):
    return v_okvirju(risba(lambda x, y: (math.floor(x), math.floor(y)) in zive,
                           x0, y0, 1, 64, 20))


def animiraj(zive, x0, y0, koraki=300):
    slika = narisi(zive, x0, y0)
    while True:
        print(slika, end='')
        time.sleep(0.05)
        print(slika.count('\n') * '\033[F', end='')
        zive = korak(zive)
        slika = narisi(zive, x0, y0)
    print(slika, end='')
