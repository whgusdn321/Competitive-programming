import sys
read = lambda :sys.stdin.readline()

N = int(read())

arr = [int(a) for a in read().split()]
b, c = map(int, read().split())

for i in range(len(arr)):
    arr[i] -= b
    if arr[i] < 0:
        arr[i] = 0

sum = 0
for item in arr:
    if item % c == 0:
        sum += item//c
    else:
        sum += (item//c + 1)

k = N + sum

print(k)