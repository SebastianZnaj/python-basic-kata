def swapPositions(lis, pos1, pos2):
    for i, x in enumerate(lis):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    lis[pos1] = elem2
    lis[pos2] = elem1
    return lis

List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))
