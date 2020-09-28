import sys
read = lambda :sys.stdin.readline().rstrip()

N = int(read())
arr = []
for _ in range(N):
    arr.append([int(a) for a in read().split()])

#print('arrr : ', arr)
for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i][0] + arr[i-1][0]
        elif j == len(arr[i])-1:
            arr[i][j] = arr[i][-1] + arr[i-1][-1]
        else:
            arr[i][j] = max(arr[i][j] + arr[i-1][j-1], arr[i][j] + arr[i-1][j])

print(max(arr[-1]))