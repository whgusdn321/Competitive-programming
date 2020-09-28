def go(x, changed):
    global H, W, k, maap, results
    if x == W + 1:
        results.append(changed)

    for i in range(0, H-k):
        c = maap[i][x]
        _changed = []
        boool = True
        for j in range(i, i+k):
            if maap[j][x] != c and j not in changed:
                _changed.append(j)
            elif maap[j][x] != c and j in changed:
                boool = False
                break
            else: # maap[j][x] == c
                continue
        if boool:
            for item in _changed:
                changed.append(item)
            go(maap, x+1, changed)
            #rewind _changed
        else:
            #rewind _changed



T = int(input())
for tc in range(1, T+1):
    H, W, k = map(int, input().split())
    maap = []
    for _ in range(H):
        temp = [int(a) for a in input().split()]
        maap.append(temp)
