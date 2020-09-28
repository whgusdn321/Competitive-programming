import sys
read = lambda :sys.stdin.readline().rstrip()

N, M, H = map(int, read().split())
W = (N*2-1)
maap = [[False]*(W) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if j%2 == 0:
            maap[i][j] = True

for _ in range(M):
    h, w = map(int, read().split())
    maap[h-1][w*2-1] = True

for _ in range(H):
    print('maap : ', maap[_])
print()

def go2(s, maap, h, H, startpoint, visited):
    if h == H-1:
        if s == startpoint:
            return True
        else:
            return False
    if 0<=s+1<W and maap[h][s+1] and not visited[h][s+1]:
        visited[h][s+1] = True
        flag = go2(s+1, maap, h, H, startpoint, visited)
    elif 0<=s-1<W and maap[h][s-1] and not visited[h][s-1]:
        visited[h][s-1] = True
        flag = go2(s-1, maap, h, H, startpoint, visited)
    else:
        visited[h+1][s] = True
        flag = go2(s, maap, h+1, H, startpoint, visited)
    return flag


def go(maap):
    flag = False
    for s in range(0, len(maap[0]), 2):
        startpoint = s
        visited = [[False]*W for _ in range(H)]
        visited[0][s] = True
        if go2(s, maap, 0 ,H, startpoint, visited):
            flag = True
        else:
            flag = False
            break
    return flag
#print(go(maap))

if go(maap):
    print(0)
    sys.exit()

for i in range(H):
    for j in range(W):
        if maap[i][j] == False:
            if 0<=j-2<W and 0<=j+2<W:
                if maap[i][j-2] == False and maap[i][j+2] == False:
                    maap[i][j] = True
                    if go(maap):
                        print(1)
                        sys.exit()
                    else:
                        maap[i][j] = False
            elif j==1 or j==W-2:
                if j == 1:
                    if len(maap[0]) == 3:
                        maap[i][j] = True
                        if go(maap):
                            print(1)
                            sys.exit()
                        else:
                            maap[i][j] = False

                    if j+2<W and maap[i][j+2] == False:
                        maap[i][j] = True

                        if go(maap):
                            print(1)
                            sys.exit()
                        else:
                            maap[i][j] = False
                else:

                    if j-2>=0 and maap[i][j-2] == False:
                        maap[i][j] = True

                        if go(maap):
                            print(1)
                            sys.exit()
                        else:
                            maap[i][j] = False


for i in range(H):
    for j in range(W):
        if maap[i][j] == False:
            if 0<=j-2<W and 0<=j+2<W:
                if maap[i][j-2] == False and maap[i][j+2] == False:
                    maap[i][j] = True

                    for l in range(H):
                        for n in range(W):
                            if maap[l][n] == False:
                                if 0 <= n - 2 < W and 0 <= n + 2 < W:
                                    if maap[l][n - 2] == False and maap[l][n + 2] == False:
                                        maap[l][n] = True
                                        if go(maap):
                                            print(2)
                                            sys.exit()
                                        else:
                                            maap[l][n] = False
                                elif n == 1 or n == W - 2:
                                    if n == 1:
                                        if len(maap[0]) == 3:
                                            maap[i][j] = True
                                            if go(maap):
                                                print(2)
                                                sys.exit()
                                            else:
                                                maap[l][n] = False

                                        if n + 2 < W and maap[l][n + 2] == False:
                                            maap[l][n] = True

                                            if go(maap):
                                                print(2)
                                                sys.exit()
                                            else:
                                                maap[l][n] = False
                                    else:
                                        if n - 2 >= 0 and maap[l][n - 2] == False:
                                            maap[l][n] = True

                                            if go(maap):
                                                print(2)
                                                sys.exit()
                                            else:
                                                maap[l][n] = False
                    maap[i][j] = False
            elif j==1 or j==W-2:
                if j == 1:
                    if len(maap[0]) == 3:
                        maap[i][j] = True

                        for l in range(H):
                            for n in range(W):
                                if maap[l][n] == False:
                                    if 0 <= n - 2 < W and 0 <= n + 2 < W:
                                        if maap[l][n - 2] == False and maap[l][n + 2] == False:
                                            maap[l][n] = True
                                            if go(maap):
                                                print(2)
                                                sys.exit()
                                            else:
                                                maap[l][n] = False
                                    elif n == 1 or n == W - 2:
                                        if n == 1:
                                            if len(maap[0]) == 3:
                                                maap[l][n] = True
                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False

                                            if n + 2 < W and maap[l][n + 2] == False:
                                                maap[l][n] = True

                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False
                                        else:

                                            if n - 2 >= 0 and maap[l][n - 2] == False:
                                                maap[l][n] = True

                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False
                        maap[i][j] = False

                    if j+2<W and maap[i][j+2] == False:
                        maap[i][j] = True

                        for l in range(H):
                            for n in range(W):
                                if maap[l][n] == False:
                                    if 0 <= l - 2 < W and 0 <= n + 2 < W:
                                        if maap[l][n - 2] == False and maap[l][n + 2] == False:
                                            maap[l][n] = True
                                            if go(maap):
                                                print(2)
                                                sys.exit()
                                            else:
                                                maap[l][n] = False
                                    elif n == 1 or n == W - 2:
                                        if n == 1:
                                            if len(maap[0]) == 3:
                                                maap[l][n] = True
                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False

                                            if n + 2 < W and maap[l][n + 2] == False:
                                                maap[l][n] = True

                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False
                                        else:

                                            if n - 2 >= 0 and maap[l][n - 2] == False:
                                                maap[l][n] = True

                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False

                        maap[i][j] = False
                else:

                    if j-2>=0 and maap[i][j-2] == False:
                        maap[i][j] = True

                        for l in range(H):
                            for n in range(W):
                                if maap[l][n] == False:
                                    if 0 <= n - 2 < W and 0 <= n + 2 < W:
                                        if maap[l][n - 2] == False and maap[l][n + 2] == False:
                                            maap[l][n] = True
                                            if go(maap):
                                                print(2)
                                                sys.exit()
                                            else:
                                                maap[l][n] = False
                                    elif n == 1 or n == W - 2:
                                        if n == 1:
                                            if len(maap[0]) == 3:
                                                maap[l][n] = True
                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False

                                            if n + 2 < W and maap[l][n + 2] == False:
                                                maap[l][n] = True

                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False
                                        else:

                                            if n - 2 >= 0 and maap[l][n - 2] == False:
                                                maap[l][n] = True

                                                if go(maap):
                                                    print(2)
                                                    sys.exit()
                                                else:
                                                    maap[l][n] = False


                        maap[i][j] = False





