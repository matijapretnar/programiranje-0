from risanje import risba, v_okvirju


def raziskuj(pogoj, x0, y0, korak):
    ukaz = ''
    while ukaz != 'q':
        print(v_okvirju(risba(pogoj, x0, y0, korak)))
        ukaz = input('ukaz (+, -, <, >, ^, v, q): ')
        if ukaz == '+':
            korak = korak / 2
        elif ukaz == '-':
            korak = korak * 2
        elif ukaz == '<':
            x0 = x0 - 16 * korak
        elif ukaz == '>':
            x0 = x0 + 16 * korak
        elif ukaz == '^':
            y0 = y0 + 12 * korak
        elif ukaz == 'v':
            y0 = y0 - 12 * korak
