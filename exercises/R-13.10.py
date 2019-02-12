X = "skullandbones"
Y = "lullabybabies"

"""
Define the subproblem: Compute the value L[j][k]

L[j][k] is the length of the longest string that is a subsequence of both X[0:j] and Y[0:k]

We have that:

    L[j][k] = 1 + L[j-1][k-1] if X[j-1] = Y[k-1]

    Increase substring length if character matches

And we have that:

    L[j][k] = max(L[j-1][k], L[j][k-1]) if X[j-1] != Y[k-1]
"""

def lcs(X, Y):
    n, m = len(X), len(Y)
    L = [[0] * (m + 1) for k in range(n + 1)]

    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j+1][k+1] = 1 + L[j][k]
            else:
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])

    return L

def lcs_string(X, Y, L):
    solution = []
    j, k = len(X), len(Y)
    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))

assert lcs_string(X, Y, lcs(X, Y)) == "ullabes"
