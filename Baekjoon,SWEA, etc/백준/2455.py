import sys
arr = []
for _ in range(4):
    a,b = [int(__) for __ in sys.stdin.readline().split()]
    arr.append([a,b])
b = [0]*4
b[0] = arr[0][1]
for i in range(1, 4):
    b[i] = b[i-1]-arr[i][0] + arr[i][1]
print(max(b))