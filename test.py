def printDiamond(n):
    s = "*"
    for i in range(1, 2 * n, 2):
        print((s * i).center(2 * n - 1))
    for i in reversed(range(1, 2 * n - 1, 2)):
        print((s * i).center(2 * n - 1))

printDiamond(8)
