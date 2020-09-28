N1, N2 = map(int, input().split())
temp1 = [char for char in input()]
temp2 = [char for char in input()]
arr = []
arr2 = []
for i in range(N1-1, -1, -1):
    arr.append(temp1[i])
    arr2.append(1)
for i in range(0, N2):
    arr.append(temp2[i])
    arr2.append(-1)

N = N1 + N2
T = int(input())

for _ in range(T):
    i = 0
    while i < N:
        if arr2[i] == 1:
            j = i + 1
            if j >= N:
                i += 1
                continue
            elif arr2[j] == arr2[i]:
                i += 1
                continue
            else:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

                temp = arr2[j]
                arr2[j] = arr2[i]
                arr2[i] = temp
                i += 2
        else:
            i += 1
for item in arr:
    print(item, end='')


