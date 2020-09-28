from copy import deepcopy
import itertools
from collections import deque

H, W = map(int, input().split())
_maap = []
for _ in range(H):
    temp = [int(char) for char in input().split()]
    _maap.append(temp)
_zeros = []
_virus = []

for i in range(H):
    for j in range(W):
        if _maap[i][j] == 0:
            _zeros.append((i, j))
        elif _maap[i][j] == 2:
            _virus.append((i, j))

num_zeros = len(_zeros) -3
results = []

for combi in itertools.combinations(_zeros, 3):
    maap = deepcopy(_maap)
    for zy, zx in combi:
        maap[zy][zx] = 1
    virus = deque(deepcopy(_virus))
    cnt = 0
    while virus:
        vy, vx = virus.popleft()
        adj = [(vy, vx-1), (vy-1, vx), (vy, vx+1), (vy+1, vx)]
        for dy, dx in adj:
            if 0<=dy<H and 0<=dx<W and maap[dy][dx] == 0:
                cnt += 1
                maap[dy][dx] = 2
                virus.append((dy, dx))

    result = num_zeros - cnt
    results.append(result)
print(max(results))

