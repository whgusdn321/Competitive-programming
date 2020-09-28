def go(i, need, bound, stakk):
    global combis
    if len(stakk) == need:
        combis.append(stakk.copy())
        return

    if i >= bound:
        return
    else:
        go(i+1, need, bound, stakk.copy())
        stakk.append(i)
        go(i+1, need, bound, stakk.copy())


N = int(input())
maap = []
for _ in range(N):
    temp = [int(a) for a in input().split()]
    maap.append(temp)
combis = []
go(0, N//2, N, [])

results = []

for combi in combis:
    hscore = 0
    ascore = 0
    away = [aw for aw in range(0, N) if aw not in combi]
    for i in range(len(combi)):
        for j in range(i+1, len(combi)):
            y = combi[i]
            x = combi[j]
            hscore += maap[y][x]
            hscore += maap[x][y]
    for i in range(len(away)):
        for j in range(i+1, len(away)):
            y = away[i]
            x = away[j]
            ascore += maap[y][x]
            ascore += maap[x][y]
    results.append(abs(hscore - ascore))
print(min(results))


