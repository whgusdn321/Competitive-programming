import sys
from collections import deque
sys.setrecursionlimit(10000000)
read = lambda :sys.stdin.readline().rstrip()

N = int(read())
maap = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)

visited = [[False]*N for _ in range(N)]
island = 0


def paint(y, x, maap, island, stack):
    global visited
    visited[y][x] = True
    maap[y][x] = island
    stack.append((y, x))
    adj = [(y, x-1), (y-1, x), (y, x+1), (y+1 , x)]
    for dy, dx in adj:
        if 0 <= dy < N and 0 <= dx < N and not visited[dy][dx]:
            if maap[dy][dx] == 1:
                paint(dy, dx, maap, island, stack)
    return stack


def bfs(toqueue):
    global visited, distances, ddiiss
    queue = deque(toqueue)
    # ((y, x), island, dis)
    for i in range(len(queue)):
        dy, dx = queue[i][0]
        visited[dy][dx] = True
    while queue:
        (py, px), pisland, pdis = queue.popleft()
        #print('pdis : ', pdis)
        adj = [(py, px-1), (py-1, px), (py, px+1), (py+1 , px)]
        for dy, dx in adj:
            if 0<=dy<N and 0<=dx<N and not visited[dy][dx]:
                maap[dy][dx] = pisland
                distances[dy][dx] = pdis + 1
                visited[dy][dx] = True
                queue.append(((dy, dx), pisland, pdis+1))
            elif 0<=dy<N and 0<=dx<N and visited[dy][dx] and maap[py][px] != maap[dy][dx]:
                #print('distances[dy][dx] :{}  distances[py][px] :{}'.format(distances[dy][dx], distances[py][px]))
                ddiiss.append(distances[dy][dx] + distances[py][px])



stacks = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and maap[i][j] == 1:
            island += 1
            #print('island : ',island)
            stack = paint(i, j, maap, island, [])
            stacks.append(stack)

toqueue = []
for i, stack in enumerate(stacks):
    for item in stack:
        toqueue.append((item, i+1, 0))

visited = [[False]*N for _ in range(N)]
distances = [[0]*N for _ in range(N)]

ddiiss = []
bfs(toqueue)
print(min(ddiiss))
#print('ddiiss : ', ddiiss)
#
# print('maap : ')
# for _ in range(N):
#     print(maap[_])
#
# print('distances : ')
# for _ in range(N):
#     print(distances[_])

