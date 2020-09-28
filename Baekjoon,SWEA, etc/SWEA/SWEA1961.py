from copy import deepcopy


def rotate90(arr, N):
    for i in range(N // 2):
        sy, sx = i, i
        l = N - 2 * i - 1
        pos = []
        value = []

        dy, dx = (0, 1)
        for _ in range(l):
            pos.append((sy, sx))
            value.append(arr[sy][sx])
            sy += dy
            sx += dx

        dy, dx = (1, 0)
        for _ in range(l):
            pos.append((sy, sx))
            value.append(arr[sy][sx])
            sy += dy
            sx += dx

        dy, dx = (0, -1)
        for _ in range(l):
            pos.append((sy, sx))
            value.append(arr[sy][sx])
            sy += dy
            sx += dx

        dy, dx = (-1, 0)
        for _ in range(l):
            pos.append((sy, sx))
            value.append(arr[sy][sx])
            sy += dy
            sx += dx

        for i in range(len(pos)):
            arr[pos[i][0]][pos[i][1]] = value[(i - l) % len(value)]
    return arr


T = int(input())
for tc in range(1, T+1):
    print('#',tc)
    N = int(input())
    arr = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        arr.append(temp)
    results = []
    for _ in range(3):
        arr = rotate90(arr, N)
        results.append(deepcopy(arr))
    for i in range(N):
        for n in range(3):
            for j in range(N):
                print(results[n][i][j], end = '')
            print(end=' ')
        print()




