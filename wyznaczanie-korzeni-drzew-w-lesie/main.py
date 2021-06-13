# DZIALA, SPRAWDZONE
from treelib import Node, Tree


def rysuj_drzewo(P):
    ilosc_drzew = 0
    drzewa = []
    for i in range(1, len(P) + 1):
        if i == P[i - 1]:
            ilosc_drzew += 1
            drzewa.append(P[i - 1])

    print("Ilość drzew: {}".format(ilosc_drzew))

    for drzewo in drzewa:
        tree = Tree()
        tree.create_node(drzewo, drzewo)  # root
        kolejne_wartosci = [drzewo]
        while kolejne_wartosci:
            szukana = kolejne_wartosci[0]
            for i in range(1, len(P) + 1):
                if szukana == P[i - 1] and szukana != i:
                    kolejne_wartosci.append(i)
                    tree.create_node(i, i, parent=szukana)

            kolejne_wartosci.remove(szukana)

        tree.show()

    return drzewa


def wszystkie_elementy(drzewa, S):
    suma = 0
    for element in drzewa:
        for el in S:
            if element == el:
                suma += 1

    return suma != len(S)


def algorytm(P):
    ilosc_operacji = [0] * len(P)
    S = [None] * len(P)

    # krok 1
    for i in range(0, len(P)):
        S[i] = P[i]

    print("S0 = {}".format(S))
    drzewa = rysuj_drzewo(S)

    # krok 2
    indeks = 1
    while wszystkie_elementy(drzewa, S):
        S1 = S.copy()
        for i in range(0, len(P)):
            if S1[i] != S1[S1[i] - 1]:
                S[i] = S1[S1[i] - 1]
                ilosc_operacji[i] += 1

        print("=================================\nS{} = {}".format(indeks, S))
        drzewa = rysuj_drzewo(S)
        indeks += 1

    print("# = {}".format(ilosc_operacji))


if __name__ == '__main__':
    P = [12, 7, 16, 7, 14, 8, 7, 16, 2, 5, 2, 12, 8, 9, 10, 12]
    algorytm(P)
