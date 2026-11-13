import random
import time

import matplotlib.pyplot as plt


def nakljucen_seznam(dolzina):
    return [random.randint(0, 10 * dolzina) for _ in range(dolzina)]


def nakljucen_narascajoc_seznam(dolzina):
    return sorted(nakljucen_seznam(dolzina))


def izmeri(f, seznam):
    klici = 0
    zacetek = time.perf_counter()
    konec = zacetek
    while konec - zacetek < 0.02:
        f(seznam)
        klici += 1
        konec = time.perf_counter()
    return (konec - zacetek) / klici


def izpisi_case(ime, velikosti, casi):
    print(ime)
    print(f'{velikosti[0]:>10}{casi[0]:12.2e} s')
    for i in range(1, len(velikosti)):
        razmerje = casi[i] / casi[i - 1]
        print(f'{velikosti[i]:>10}{casi[i]:12.2e} s{razmerje:8.1f}')


def narisi_case(imena, velikosti, vsi_casi):
    for ime, casi in zip(imena, vsi_casi):
        plt.plot(velikosti, casi, 'o-', label=ime)
    plt.xlabel('dolžina seznama')
    plt.ylabel('čas [s]')
    plt.legend()
    plt.show()


def primerjaj(funkcije, velikosti, naredi_seznam=nakljucen_seznam):
    imena = [f.__name__ for f in funkcije]
    vsi_casi = []
    for f in funkcije:
        casi = [izmeri(f, naredi_seznam(n)) for n in velikosti]
        izpisi_case(f.__name__, velikosti, casi)
        vsi_casi.append(casi)
    narisi_case(imena, velikosti, vsi_casi)
