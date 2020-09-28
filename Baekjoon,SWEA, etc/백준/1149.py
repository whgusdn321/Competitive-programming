import sys
read = lambda :sys.stdin.readline().rstrip()

N = int(read())
arr = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    arr.append(temp)

sums = [0, 0, 0, 0, 0, 0]

for i in range(0, N, 3):
    print('i : ',i)
    sums[0] += arr[i][0]
    sums[0] += arr[i+1][1]
    sums[0] += arr[i+2][2]

for i in range(0, N, 3):
    sums[1] += arr[i][0]
    sums[1] += arr[i+1][2]
    sums[1] += arr[i+2][1]

for i in range(0, N, 3):
    sums[2] += arr[i][1]
    sums[2] += arr[i+1][0]
    sums[2] += arr[i+2][2]

for i in range(0, N, 3):
    sums[3] += arr[i][1]
    sums[3] += arr[i+1][2]
    sums[3] += arr[i+2][0]

for i in range(0, N, 3):
    sums[4] += arr[i][2]
    sums[4] += arr[i+1][1]
    sums[4] += arr[i+2][0]

for i in range(0, N, 3):
    sums[5] += arr[i][2]
    sums[5] += arr[i+1][0]
    sums[5] += arr[i+2][1]

print(sums)