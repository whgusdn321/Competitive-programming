

def is_possible(i, j):
    global maap, H, W
    if i == H-1 or j == W-1:
        return False
    else:
        for _i in range(i, i+2):
            for _j in range(j, j+2):
                if maap[_i][_j] == 1:
                    return False
        return True


def go(i, maap, cnt):
    global N, possibles, results
    if i == N:
        results.append(cnt)
        return
    py, px = possibles[i]

    boool = False
    for ii in range(py, py+2):
        for jj in range(px, px+2):
            if maap[ii][jj] == 1:
                boool = True
    if boool:
        go(i+1, maap, cnt)
    else:
        for ii in range(py, py+2):
            for jj in range(px, px+2):
                maap[ii][jj] = 1
        go(i+1, maap, cnt+1)
        for ii in range(py, py+2):
            for jj in range(px, px+2):
                maap[ii][jj] = 0
        if is_possible(py, px+1) or is_possible(py+1, px) or is_possible(py+1, px+1):
            go(i+1, maap, cnt)




T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    maap = []
    for _ in range(H):
        temp = [int(a) for a in input().split()]
        maap.append(temp)
    possibles = []
    for i in range(H):
        for j in range(W):
            if is_possible(i, j):
                possibles.append((i, j))
    N = len(possibles)
    #print('possibles : ',possibles)
    results = []
    go(0, maap, 0)
    #print('results : ',results)
    print('#', tc, end=' ')
    print(max(results))
