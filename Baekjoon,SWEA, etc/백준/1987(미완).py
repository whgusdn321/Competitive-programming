import sys
H, W = map(int, sys.stdin.readline().rstrip().split())
maap = []
visited = []
alp_vist = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False, 'I': False, 'J': False, \
            'K': False, 'L': False, 'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False, 'S': False, 'T': False, \
            'U': False, 'V': False, 'W': False, 'X': False, 'Y': False, 'Z': False}

for _ in range(H):
    temp = [a for a in sys.stdin.readline().rstrip()]
    maap.append(temp)
    temp2 = [False]*W
    visited.append(temp2)

lengths = []


def backtrack(y, x, cnt):
    global alp_vist, maap
    if not alp_vist[maap[y][x]]: #부모가 가능하다면,
        alp_vist[maap[y][x]] = True
        cnt += 1
        adjacent = [[y, x-1], [y-1, x], [y, x+1], [y+1, x]]
        for ny, nx in adjacent:
            if 0 <= ny < H and 0 <= nx < W:
                backtrack(ny, nx, cnt) #한번 가봐라..
        alp_vist[maap[y][x]] = False
    else: #갔더니  더 못가면
        lengths.append(cnt)
        return


def dfs(cy, cx, cnt):
    global alp_vist, lengths, visited
    adjacent = [[cy, cx-1], [cy-1, cx], [cy, cx+1], [cy+1, cx]]
    lengths.append(cnt)
    for ny, nx in adjacent:
        if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx]:
            if not alp_vist[maap[ny][nx]]:
                alp_vist[maap[ny][nx]] = True
                cnt += 1
                visited[ny][nx] = True
                dfs(ny, nx, cnt)
                visited[ny][nx] = False
                alp_vist[maap[ny][nx]] = False
                cnt -= 1
    #print('sofar alp_visit: ', alp_vist)

#alp_vist[maap[0][0]] = True
#visited[0][0] = True
#cnt = 1
#dfs(0, 0, cnt)
backtrack(0, 0, 0)
print(max(lengths))
#print('sofar alp_visit: ',alp_vist)

