def sort_stack(stkA):
    stkB = []
    while stkA:
        top = stkA.pop()
        while stkB and stkB[-1] < top:
            stkA.append(stkB.pop())
        stkB.append(top)
    while stkB:
        stkA.append(stkB.pop())


def main():
    stkA = [1, 8, 4, 5, 8, 2, 4, 5, 3]
    sort_stack(stkA)
    print(stkA)


main()
