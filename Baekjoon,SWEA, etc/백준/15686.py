import sys
import itertools
read = lambda :sys.stdin.readline().rstrip()

N, M = map(int, read().split())

maap = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)

ones = []
twos = []

for i in range(N):
    for j in range(N):
        if maap[i][j] == 1 :
            ones.append((i, j))
        if maap[i][j] == 2:
            twos.append((i, j))

combis = []

#combis = itertools.combinations([i for i in range(0, len(twos))], M)


def combi(i, stack):
    global M, combis, twos
    if len(stack) == M:
        combis.append(stack.copy())
        return
    else:
        for j in range(i+1, len(twos)):
            stack.append(j)
            combi(j, stack)
            stack.pop()

combi(-1, [])
real_chicks = []
for combi in combis:
    new_twos = []
    for item in combi:
        new_twos.append(twos[item])
    ls = []
    for i in range(len(ones)):
        distances = []
        for j in range(len(new_twos)):
            dist = abs(ones[i][0] - new_twos[j][0]) +\
                    abs(ones[i][1] - new_twos[j][1])
            distances.append(dist)
        ls.append(min(distances))
    real_chicks.append(sum(ls))

print(min(real_chicks))

