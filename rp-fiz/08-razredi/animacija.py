import time


def animiraj(stanje, korak, narisi, premor=0.03):
    slika = narisi(stanje)
    print(slika, end='')
    while True:
        time.sleep(premor)
        korak(stanje)
        gor = slika.count('\n') * '\033[F'
        slika = narisi(stanje)
        print(gor + slika, end='')
