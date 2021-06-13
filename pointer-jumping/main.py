def tree_in_wood(P):
    print("WYZNACZENIE KORZENI W DRZEWIE")
    roots = _get_roots(P)
    iteration = 1
    while not _contains_only_roots(P, roots):
        print("ITERATION {}".format(iteration))
        P = _next_iteration(P)
        iteration += 1


def sufix_list(NEXT, W):
    print("SUMY SUFIKSOWE NA LIŚCIE")
    iteration = 1
    Q = NEXT
    while not _contains_only_0(Q):
        print("ITERATION {}".format(iteration))
        W = _next_sufix_W(Q, W)
        Q = _next_iteration_Q(Q)
        iteration += 1


def prefix_list(NEXT, W):
    print("SUMY PREFIKSOWE NA LIŚĆIE")
    iteration = 1
    Q = NEXT
    while not _contains_only_0(Q):
        print("ITERATION {}".format(iteration))
        W = _next_prefix_W(Q, W)
        Q = _next_iteration_Q(Q)
        iteration += 1


def _next_sufix_W(Q, W):
    temp = []
    for i in range(len(Q)):
        if Q[i] == 0:
            temp.append(W[i])
        else:
            temp.append(W[i] + W[Q[i]-1])
    print("W = {}".format(temp))
    return temp


def _next_prefix_W(Q, W):
    temp = [None] * len(W)
    for i in range(len(Q)):
        if Q[i] != 0:
            temp[Q[i]-1] = W[i] + W[Q[i]-1]
    for i, val in enumerate(temp):
        if val is None:
            temp[i] = W[i]
    print("W = {}".format(temp))
    return temp


def _next_iteration_Q(Q):
    temp = []
    for i in range(len(Q)):
        if Q[i] == 0:
            temp.append(Q[i])
        else:
            temp.append(Q[Q[i]-1])
    print("Q = {}".format(temp))
    return temp


def _next_iteration(P):
    temp = []
    for i in range(len(P)):
        temp.append(_tree_in_woods_loop(P, i))
    print(temp)
    return temp


def _get_roots(P):
    roots = []
    for i in range(len(P)):
        if P[i] == i+1:
            roots.append(i+1)
    return roots


def _contains_only_roots(P, roots):
    for i in P:
        if i not in roots:
            return False
    return True


def _contains_only_0(P):
    for i in P:
        if i != 0:
            return False
    return True


def _tree_in_woods_loop(S, i):
    if S[i-1] != S[S[i]-1]:
        return S[S[i]-1]
    else:
        return S[i-1]

if __name__ == "__main__":

    # Przykład z ćwiczeń wyznaczania drzewa w lesie
    # P = [12,7,16,7,14,8,7,16,2,5,2,12,8,9,10,12]
    # tree_in_wood(P)

    # Przykład z ćwiczeń sum sufiksowych
    # NEXT = [5,4,8,7,3,1,6,0]
    # W = [3,5,2,1,7,2,1,2]
    # Przykład z powtórki sum sufiksowych
    NEXT = [3,1,8,2,6,0,4,5]
    W = [2,4,5,6,3,1,5,2]
    sufix_list(NEXT,W)
    #
    # # Przykład z ćwiczeń sum prefiksowych
    # NEXT = [6,8,1,0,7,4,2,3]
    # W = [3,2,1,1,2,3,3,2]
    # prefix_list(NEXT, W)
