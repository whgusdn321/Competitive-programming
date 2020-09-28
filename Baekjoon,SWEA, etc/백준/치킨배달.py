def make_combis(i, stakk):
    global combis, M, N, twos
    if len(stakk) == M:
        combis.append(stakk.copy())
        return
    for j in range(i+1, N):
        stakk.append(twos[j])
        make_combis(j, stakk)
        stakk.pop()


N, M = map(int, input().split())
maap = []
ones = []
twos = []
for _ in range(N):
    temp = [int(char) for char in input().split()]
    maap.append(temp)

for i in range(N):
    for j in range(N):
        if maap[i][j] == 1:
            ones.append((i, j))
        elif maap[i][j] == 2:
            twos.append((i, j))

N = len(twos)
combis = []
make_combis(-1, [])
results = []

for combi in combis:
    result = []
    for oy, ox in ones:
        chicken_dis = []
        for cy, cx in combi:
            dis = abs(cy-oy) + abs(cx-ox)
            chicken_dis.append(dis)
        result.append(min(chicken_dis))
    results.append(sum(result))

print(min(results))