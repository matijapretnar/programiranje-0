from risanje import risba, v_okvirju
from animacija import animiraj

SIRINA = 64
VISINA = 48
G = 50
DT = 0.05


class Telo:
    def __init__(self, masa, x, y, vx, vy, polmer):
        self.masa = masa
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.polmer = polmer

    def __repr__(self):
        return (f'Telo({self.masa}, {self.x}, {self.y}, '
                f'{self.vx}, {self.vy}, {self.polmer})')

    def deluj(self, fx, fy, dt):
        self.vx = self.vx + fx / self.masa * dt
        self.vy = self.vy + fy / self.masa * dt

    def premakni(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

    def odbij_od_sten(self, sirina, visina):
        # Telo je že za steno, zato ga prezrcalimo nazaj, skupaj s hitrostjo.
        if self.x < self.polmer and self.vx < 0:
            self.x = 2 * self.polmer - self.x
            self.vx = -self.vx
        if self.x > sirina - self.polmer and self.vx > 0:
            self.x = 2 * (sirina - self.polmer) - self.x
            self.vx = -self.vx
        if self.y < self.polmer and self.vy < 0:
            self.y = 2 * self.polmer - self.y
            self.vy = -self.vy
        if self.y > visina - self.polmer and self.vy > 0:
            self.y = 2 * (visina - self.polmer) - self.y
            self.vy = -self.vy

    def vsebuje(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.polmer ** 2


zoge = [
    Telo(1, 10, 40, 12, 0, 2),
    Telo(2, 30, 30, -20, 10, 3),
    Telo(1, 50, 10, 5, 30, 1.5),
]


def korak(zoge):
    for zoga in zoge:
        # Najprej sila spremeni hitrost, nato nova hitrost premakne žogo.
        # V obratnem vrstnem redu bi energija naraščala in žoge bi
        # odskakovale vse višje.
        zoga.deluj(0, -zoga.masa * G, DT)
        zoga.premakni(DT)
        zoga.odbij_od_sten(SIRINA, VISINA)


def je_v_kateri(telesa, x, y):
    for telo in telesa:
        if telo.vsebuje(x, y):
            return True
    return False


def narisi(zoge):
    return v_okvirju(risba(lambda x, y: je_v_kateri(zoge, x, y),
                           SIRINA / 2, VISINA / 2, 1, SIRINA, VISINA // 2))

def demo():
    animiraj(zoge, korak, narisi)