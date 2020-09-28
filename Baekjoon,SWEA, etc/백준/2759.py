import sys
from collections import deque
read = lambda :sys.stdin.readline().rstrip()
N = int(read())

arr = []
for _ in range(N):
    arr.append(int(read()))

memo = [[arr[0]], [arr[1], arr[0]+arr[1]]]

for i in range(2, N):
    temp = []
    for item in memo[i-2]:
        temp.append(item+arr[i])
    for j in range(0, len(memo[i-1])-1):
        temp.append(memo[i-1][j] + arr[i])
    memo.append(temp)
    memo[i-1] =[max(memo[i-1])]

#print('memo : ', memo)
print(max(memo[-1]))