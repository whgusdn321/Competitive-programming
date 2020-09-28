import sys
read = lambda :sys.stdin.readline()

N = int(read())
maap = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)

stack1 = []
stack2 = []
visited= [[False] * N for _ in range(N)]


def go(y, x, stack1, stack2, i):
    if y == x:
        return
    #termiation
    if len(stack1) == len(stack2) == 
    #mark as visited
    if not:
        visited[y][x] = True
    #append to stack
for i in range(N):
    for j in range(N):
        go(i, j, stack1, stack2)