import math
from risanje import v_okvirju
from risanje_sledi import risba
from animacija import animiraj
from zoge_polravnine import Vektor, Telo

G = 1
DT = 0.05
SIRINA = 64
VISINA = 48

sled = set()


def gravitacija(telo, drugo):
    r = drugo.polozaj - telo.polozaj
    # Ko se telesi prekrivata, sila ne raste več, sicer bi bližnja
    # srečanja zaradi koraka DT izstrelila telesi.
    d = max(abs(r), telo.polmer + drugo.polmer)
    return (G * telo.masa * drugo.masa / d ** 3) * r


def korak(telesa):
    # Najprej izračunamo vse sile in šele nato premaknemo telesa,
    # sicer bi bil rezultat odvisen od vrstnega reda teles.
    sile = []
    for i in range(len(telesa)):
        sila = Vektor(0, 0)
        for j in range(len(telesa)):
            if i != j:
                sila = sila + gravitacija(telesa[i], telesa[j])
        sile.append(sila)
    for telo, sila in zip(telesa, sile):
        telo.deluj(sila, DT)
        telo.premakni(DT)
        sled.add((math.floor(2 * telo.polozaj.x), math.floor(2 * telo.polozaj.y)))


def je_telo(telesa, tocka):
    return any(telo.vsebuje(tocka) for telo in telesa)


def je_sled(tocka):
    return (math.floor(2 * tocka.x), math.floor(2 * tocka.y)) in sled


def narisi(telesa):
    return v_okvirju(risba(lambda x, y: je_telo(telesa, Vektor(x, y)),
                           lambda x, y: je_sled(Vektor(x, y)),
                           0, 0, 1, SIRINA, VISINA // 2))


def soncni_sistem():
    sonce = Telo(1000, Vektor(0, 0), Vektor(0, 0), 2)
    planeti = []
    for r in [8, 14, 20]:
        v = (G * sonce.masa / r) ** 0.5
        planeti.append(Telo(1, Vektor(r, 0), Vektor(0, v), 1))
    return [sonce] + planeti


def osmica():
    # Tri enaka telesa, ki se lovijo po osmici (Moore 1993,
    # Chenciner in Montgomery 2000).
    x = Vektor(14.5500654, -3.64631295)
    v = Vektor(-9.3240737, -8.6473146)
    return [
        Telo(1500, x, -0.5 * v, 1),
        Telo(1500, -x, -0.5 * v, 1),
        Telo(1500, Vektor(0, 0), v, 1),
    ]


def pitagorejski():
    # Telesa z masami 3, 4 in 5 mirujejo v ogliščih pravokotnega
    # trikotnika s stranicami 3, 4 in 5 (Burrau 1913). Gibanje je kaotično,
    # zato ga s stalnim korakom DT izračunamo le približno.
    return [
        Telo(90, Vektor(4, 12), Vektor(0, 0), 1),
        Telo(120, Vektor(-8, -4), Vektor(0, 0), 1),
        Telo(150, Vektor(4, -4), Vektor(0, 0), 1),
    ]


def demo1():
    sled.clear()
    animiraj(soncni_sistem(), korak, narisi)

def demo2():
    sled.clear()
    animiraj(osmica(), korak, narisi)

def demo3():
    sled.clear()
    animiraj(pitagorejski(), korak, narisi)
