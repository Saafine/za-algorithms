# DZIALA, SPRAWDZONE
# sumy prefiksowe to zadanie 4 cw5
def wszedzie_zera(Q1):
    return Q1.count(0) != len(Q1)


def rysuj(Q, W, szukaj):
    # 1. znajdz liczbe, ktora nie wystepuje w tablicy
    liczba = 0

    if szukaj:
        for i in range(0, len(Q)):
            if Q.count(i) == 0:
                liczba = i
                break

    # 2. lec od znalezionej liczby, az do konca
    for i in range(0, len(Q)):
        if szukaj:
            kolejnosc.append(liczba)
        else:
            liczba = kolejnosc[i]
        print("({})[{}][•]".format(liczba, W[liczba - 1]), end='\t\t')
        if szukaj:
            liczba = Q[liczba - 1]


def algorytm(Q, W):
    ilosc_operacji = [0] * len(Q)

    print("Krok 0)\tQ = {}".format(Q))
    print("\t\tW = {}".format(W))

    rysuj(Q, W, True)

    indeks = 1
    while wszedzie_zera(Q):
        Q1 = Q.copy()
        W1 = W.copy()
        for i in range(0, len(Q1)):
            if Q1[i] != 0:
                W[Q1[i] - 1] = W1[i] + W1[Q[i] - 1]
                Q[i] = Q1[Q1[i] - 1]
                ilosc_operacji[i] += 1

        print("\n\n=================================\nKrok {})\tQ = {}".format(indeks, Q))
        print("\t\tW = {}\n".format(W))
        rysuj(Q, W, False)
        indeks += 1

    print("\n\n# = {}".format(ilosc_operacji))
    print("EREW PRAM")
    print("T(n) = Θ(logn)")
    print("W(n) = Θ(nlogn) <--- nie optymalny")
    print("P(n) = n")


kolejnosc = []

if __name__ == '__main__':
    Q = [6, 8, 1, 0, 7, 4, 2, 3]
    W = [3, 2, 1, 1, 2, 3, 3, 2]

    algorytm(Q, W)
