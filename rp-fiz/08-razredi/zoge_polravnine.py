from risanje import risba, v_okvirju
from animacija import animiraj

SIRINA = 64
VISINA = 48
DT = 0.05


class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vektor({self.x}, {self.y})'

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vektor(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, skalar):
        return Vektor(self.x * skalar, self.y * skalar)

    def __rmul__(self, skalar):
        return self * skalar

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return (self @ self) ** 0.5


class Polravnina:
    # Normala kaže iz polravnine, proti prostoru, po katerem letijo žoge.
    def __init__(self, tocka, normala):
        self.tocka = tocka
        self.normala = (1 / abs(normala)) * normala

    def __repr__(self):
        return f'Polravnina({self.tocka}, {self.normala})'

    def razdalja(self, tocka):
        return (tocka - self.tocka) @ self.normala

    def vsebuje(self, tocka):
        return self.razdalja(tocka) <= 0


class Telo:
    def __init__(self, masa, polozaj, hitrost, polmer):
        self.masa = masa
        self.polozaj = polozaj
        self.hitrost = hitrost
        self.polmer = polmer

    def __repr__(self):
        return (f'Telo({self.masa}, {self.polozaj}, '
                f'{self.hitrost}, {self.polmer})')

    def deluj(self, sila, dt):
        self.hitrost = self.hitrost + (dt / self.masa) * sila

    def premakni(self, dt):
        self.polozaj = self.polozaj + dt * self.hitrost

    def odbij(self, polravnina):
        # Telo je že v polravnini, zato ga prezrcalimo nazaj, skupaj s hitrostjo.
        n = polravnina.normala
        globina = self.polmer - polravnina.razdalja(self.polozaj)
        if globina > 0 and self.hitrost @ n < 0:
            self.polozaj = self.polozaj + 2 * globina * n
            self.hitrost = self.hitrost - 2 * (self.hitrost @ n) * n

    def vsebuje(self, tocka):
        return abs(tocka - self.polozaj) <= self.polmer


G = Vektor(0, -50)

stene = [
    Polravnina(Vektor(0, 0), Vektor(1, 0)),
    Polravnina(Vektor(SIRINA, 0), Vektor(-1, 0)),
    Polravnina(Vektor(0, 0), Vektor(0, 1)),
    Polravnina(Vektor(0, VISINA), Vektor(0, -1)),
]

klanca = [
    Polravnina(Vektor(0, 16), Vektor(1, 2)),
    Polravnina(Vektor(SIRINA, 16), Vektor(-1, 2)),
]

polravnine = stene + klanca

zoge = [
    Telo(1, Vektor(10, 40), Vektor(12, 0), 2),
    Telo(2, Vektor(30, 30), Vektor(-20, 10), 3),
    Telo(1, Vektor(50, 30), Vektor(5, 30), 1.5),
]


def korak(zoge):
    for zoga in zoge:
        # Najprej sila spremeni hitrost, nato nova hitrost premakne žogo.
        # V obratnem vrstnem redu bi energija naraščala in žoge bi
        # odskakovale vse višje.
        zoga.deluj(zoga.masa * G, DT)
        zoga.premakni(DT)
        for polravnina in polravnine:
            zoga.odbij(polravnina)


def je_na_sliki(zoge, tocka):
    return any(lik.vsebuje(tocka) for lik in zoge + polravnine)


def narisi(zoge):
    return v_okvirju(risba(lambda x, y: je_na_sliki(zoge, Vektor(x, y)),
                           SIRINA / 2, VISINA / 2, 1, SIRINA, VISINA // 2))

def demo():
    animiraj(zoge, korak, narisi)