def rotate(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp


def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])
    print()


def solution(key, lock):
    to_fill = 0
    N = len(lock)
    m = len(key)
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                to_fill += 1

    for _ in range(4):
        rotate(key)
        # printMatrix(key)
        for ky in range(-m+1, N):
            for kx in range(-m+1, N):
                _pos = True
                cnt = 0
                for h in range(m):
                    for w in range(m):
                        ly = ky + h
                        lx = kx + w
                        if 0<=ly<N and 0<=lx<N\
                            and not (key[h][w] ^ lock[ly][lx]):
                            _pos = False
                        elif 0<=ly<N and 0<=lx<N\
                            and key[h][w] and not lock[ly][lx]:
                            cnt += 1
                        elif 0<=ly<N and 0<=lx<N\
                            and not key[h][w] and lock[ly][lx]:
                            continue
                        else:
                            pass
                if _pos and cnt == to_fill:
                    return True
                else:
                    continue
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
