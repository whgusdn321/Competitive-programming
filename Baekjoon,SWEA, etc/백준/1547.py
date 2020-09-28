import sys
read = lambda :sys.stdin.readline().rstrip()

M = int(read())
cups = [0, 1, 2, 3]
for _ in range(M):
    a, b = map(int, read().split())
    temp = cups[a]
    cups[a] = cups[b]
    cups[b] = temp
for i in range(4):
    if cups[i] == 1:
        print(i)