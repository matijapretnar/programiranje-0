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

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


G = Vektor(0, -50)


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

    def odbij_od_sten(self, sirina, visina):
        # Telo je že za steno, zato ga prezrcalimo nazaj, skupaj s hitrostjo.
        x, y = self.polozaj.x, self.polozaj.y
        vx, vy = self.hitrost.x, self.hitrost.y
        if x < self.polmer and vx < 0:
            x, vx = 2 * self.polmer - x, -vx
        if x > sirina - self.polmer and vx > 0:
            x, vx = 2 * (sirina - self.polmer) - x, -vx
        if y < self.polmer and vy < 0:
            y, vy = 2 * self.polmer - y, -vy
        if y > visina - self.polmer and vy > 0:
            y, vy = 2 * (visina - self.polmer) - y, -vy
        self.polozaj = Vektor(x, y)
        self.hitrost = Vektor(vx, vy)

    def vsebuje(self, tocka):
        return abs(tocka - self.polozaj) <= self.polmer


zoge = [
    Telo(1, Vektor(10, 40), Vektor(12, 0), 2),
    Telo(2, Vektor(30, 30), Vektor(-20, 10), 3),
    Telo(1, Vektor(50, 10), Vektor(5, 30), 1.5),
]


def korak(zoge):
    for zoga in zoge:
        # Najprej sila spremeni hitrost, nato nova hitrost premakne žogo.
        # V obratnem vrstnem redu bi energija naraščala in žoge bi
        # odskakovale vse višje.
        zoga.deluj(zoga.masa * G, DT)
        zoga.premakni(DT)
        zoga.odbij_od_sten(SIRINA, VISINA)


def je_v_kateri(telesa, tocka):
    for telo in telesa:
        if telo.vsebuje(tocka):
            return True
    return False


def narisi(zoge):
    return v_okvirju(risba(lambda x, y: je_v_kateri(zoge, Vektor(x, y)),
                           SIRINA / 2, VISINA / 2, 1, SIRINA, VISINA // 2))

def demo():
    animiraj(zoge, korak, narisi)