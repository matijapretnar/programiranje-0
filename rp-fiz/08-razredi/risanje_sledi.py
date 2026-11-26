import risanje


def znak_sledi(pogoj, x, y, dx, dy):
    # ⠁ 1   ⠈ 8
    # ⠂ 2   ⠐ 16
    # ⠄ 4   ⠠ 32
    # ⡀ 64  ⢀ 128
    biti = [(0, 0, 1), (0, 1, 2), (0, 2, 4), (1, 0, 8),
            (1, 1, 16), (1, 2, 32), (0, 3, 64), (1, 3, 128)]
    indeks = 0
    for stolpec, vrstica, bit in biti:
        if pogoj(x + (stolpec - 0.5) * dx / 2, y + (1.5 - vrstica) * dy / 4):
            indeks += bit
    if indeks == 0:
        return ' '
    return chr(0x2800 + indeks)


def znak(spredaj, zadaj, x, y, dx, dy):
    # Telesa narišemo s kvadranti; kjer jih ni, narišemo sled z Braillovimi pikami.
    kvadrant = risanje.znak(spredaj, x, y, dx, dy)
    if kvadrant != ' ':
        return kvadrant
    return znak_sledi(zadaj, x, y, dx, dy)


def risba(spredaj, zadaj, x0, y0, korak, stolpci=64, vrstice=24):
    slika = ''
    for i in range(vrstice):
        y = y0 + (vrstice / 2 - i - 0.5) * 2 * korak
        for j in range(stolpci):
            x = x0 + (j + 0.5 - stolpci / 2) * korak
            slika += znak(spredaj, zadaj, x, y, korak, 2 * korak)
        slika += '\n'
    return slika
