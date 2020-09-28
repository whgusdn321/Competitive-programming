def inspect(arr, N, L):
    visited = [False] * N
    i = 0
    while i < N-1:
        j = i + 1
        if arr[i] == arr[j]:
            i += 1
            continue
        else:
            if arr[i] == arr[j] + 1:
                boool = True
                for jj in range(j, j+L):
                    if jj < N and arr[jj] == arr[j] and not visited[jj]:
                        boool &= True
                    else:
                        boool &= False
                if boool:
                    for jj in range(j, j+L):
                        visited[jj] = True
                    i = j+L-1
                    continue
                else:
                    return False
            elif arr[i] == arr[j] - 1:
                boool = True
                for ii in range(i, i-L, -1):
                    if ii >= 0 and arr[ii] == arr[i] and not visited[ii]:
                        boool &= True
                    else:
                        boool &= False
                if boool:
                    for ii in range(i, i-L, -1):
                        visited[ii] = True
                    i = i + 1
                    continue
                else:
                    return False
            else:
                return False
    if i == N-1:
        return True



N, L = map(int, input().split())
maap = []
for _ in range(N):
    temp = [int(char) for char in input().split()]
    maap.append(temp)

cnt = 0
for i in range(N):
    inspect_arr = maap[i]
    if inspect(inspect_arr, N, L):
        cnt += 1
for j in range(N):
    inspect_arr = [maap[i][j] for i in range(N)]
    if inspect(inspect_arr, N, L):
        cnt += 1
print(cnt)





