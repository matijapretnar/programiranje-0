from risanje import risba, v_okvirju
from animacija import animiraj

SIRINA = 64
VISINA = 48
G = 50
DT = 0.05

zoge = [
    {'masa': 1, 'x': 10, 'y': 40, 'vx': 12, 'vy': 0, 'polmer': 2},
    {'masa': 2, 'x': 30, 'y': 30, 'vx': -20, 'vy': 10, 'polmer': 3},
    {'masa': 1, 'x': 50, 'y': 10, 'vx': 5, 'vy': 30, 'polmer': 1.5},
]


def korak(zoge):
    for zoga in zoge:
        fx = 0
        fy = -zoga['masa'] * G
        # Najprej sila spremeni hitrost, nato nova hitrost premakne žogo.
        # V obratnem vrstnem redu bi energija naraščala in žoge bi
        # odskakovale vse višje.
        zoga['vx'] = zoga['vx'] + fx / zoga['masa'] * DT
        zoga['vy'] = zoga['vy'] + fy / zoga['masa'] * DT
        zoga['x'] = zoga['x'] + zoga['vx'] * DT
        zoga['y'] = zoga['y'] + zoga['vy'] * DT
        # Žoga je že za steno, zato jo prezrcalimo nazaj, skupaj s hitrostjo.
        if zoga['x'] < zoga['polmer'] and zoga['vx'] < 0:
            zoga['x'] = 2 * zoga['polmer'] - zoga['x']
            zoga['vx'] = -zoga['vx']
        if zoga['x'] > SIRINA - zoga['polmer'] and zoga['vx'] > 0:
            zoga['x'] = 2 * (SIRINA - zoga['polmer']) - zoga['x']
            zoga['vx'] = -zoga['vx']
        if zoga['y'] < zoga['polmer'] and zoga['vy'] < 0:
            zoga['y'] = 2 * zoga['polmer'] - zoga['y']
            zoga['vy'] = -zoga['vy']
        if zoga['y'] > VISINA - zoga['polmer'] and zoga['vy'] > 0:
            zoga['y'] = 2 * (VISINA - zoga['polmer']) - zoga['y']
            zoga['vy'] = -zoga['vy']


def je_v_zogi(zoge, x, y):
    for zoga in zoge:
        if (x - zoga['x']) ** 2 + (y - zoga['y']) ** 2 <= zoga['polmer'] ** 2:
            return True
    return False


def narisi(zoge):
    return v_okvirju(risba(lambda x, y: je_v_zogi(zoge, x, y),
                           SIRINA / 2, VISINA / 2, 1, SIRINA, VISINA // 2))

def demo():
    animiraj(zoge, korak, narisi)