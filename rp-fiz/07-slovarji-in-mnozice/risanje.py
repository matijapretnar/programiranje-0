def znak(pogoj, x, y, dx, dy):
    # ▘ 1   ▝ 2
    # ▖ 4   ▗ 8
    zgoraj_levo = pogoj(x - dx / 4, y + dy / 4)
    zgoraj_desno = pogoj(x + dx / 4, y + dy / 4)
    spodaj_levo = pogoj(x - dx / 4, y - dy / 4)
    spodaj_desno = pogoj(x + dx / 4, y - dy / 4)
    indeks = (int(zgoraj_levo) + 2 * int(zgoraj_desno)
              + 4 * int(spodaj_levo) + 8 * int(spodaj_desno))
    return ' ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█'[indeks]


def risba(pogoj, x0, y0, korak, stolpci=64, vrstice=24):
    slika = ''
    for i in range(vrstice):
        y = y0 + (vrstice / 2 - i - 0.5) * 2 * korak
        for j in range(stolpci):
            x = x0 + (j + 0.5 - stolpci / 2) * korak
            slika += znak(pogoj, x, y, korak, 2 * korak)
        slika += '\n'
    return slika


def v_okvirju(slika):
    sirina = slika.find('\n')
    vrh = '┌' + sirina * '─' + '┐\n'
    dno = '└' + sirina * '─' + '┘\n'
    return vrh + '│' + slika[:-1].replace('\n', '│\n│') + '│\n' + dno
