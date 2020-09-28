T = int(input())


def go(char, y, x):
    global maap, results

    if y < 0 or y >= 4 or x < 0 or x >= 4 :
        return

    char += str(maap[y][x])
    if len(char) == 7:
        if char not in results:
            results.append(char)
        return
    adj = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for dy, dx in adj:
        go(char, dy, dx)


for tc in range(1, T+1):
    maap =[]
    for _ in range(4):
        temp = [int(a) for a in input().split()]
        maap.append(temp)

    results = []
    for i in range(4):
        for j in range(4):
            go("", i, j)
    print('#{} {}'.format(tc, len(results)))
