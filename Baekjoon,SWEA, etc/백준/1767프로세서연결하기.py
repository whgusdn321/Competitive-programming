def go(node, maap, length, cnt):
    global num_nodes, results

    if node == num_nodes:
        if cnt > results[0]:
            results = (cnt, length)
        elif cnt == results[0]:
            if length < results[1]:
                results = (cnt, length)
        else:
            pass
        return

    for dir in ['up', 'down', 'left', 'right']:
        if dir == 'up':
            core_y, core_x = position[node][0], position[node][1]
            sy, sx = core_y - 1, core_x

            while sy >= 0 and maap[sy][sx] == 0:
                maap[sy][sx] = 1
                length += 1
                sy -= 1

            if sy >= 0:
                for _sy in range(sy+1, core_y):
                    maap[_sy][sx] = 0
                    length -= 1
                go(node+1, maap, length, cnt)
            else:
                go(node+1, maap, length, cnt+1)
                for _sy in range(sy+1, core_y):
                    maap[_sy][sx] = 0
                    length -= 1
        elif dir == 'down':
            core_y, core_x = position[node][0], position[node][1]
            sy, sx = core_y + 1, core_x

            while sy < N and maap[sy][sx] == 0:
                maap[sy][sx] = 1
                length += 1
                sy += 1

            if sy < N:
                for _sy in range(sy - 1, core_y, -1):
                    maap[_sy][sx] = 0
                    length -= 1
                go(node + 1, maap, length, cnt)
            else:
                go(node + 1, maap, length, cnt + 1)
                for _sy in range(sy - 1, core_y, -1):
                    maap[_sy][sx] = 0
                    length -= 1
        elif dir == 'left':
            core_y, core_x = position[node][0], position[node][1]
            sy, sx = core_y, core_x-1

            while sx >= 0 and maap[sy][sx] == 0:
                maap[sy][sx] = 1
                length += 1
                sx -= 1

            if sx >= 0:
                for _sx in range(sx + 1, core_x):
                    maap[sy][_sx] = 0
                    length -= 1
                go(node + 1, maap, length, cnt)
            else:
                go(node + 1, maap, length, cnt + 1)
                for _sx in range(sx + 1, core_x):
                    maap[sy][_sx] = 0
                    length -= 1
        else: #right
            core_y, core_x = position[node][0], position[node][1]
            sy, sx = core_y, core_x + 1

            while sx < N and maap[sy][sx] == 0:
                maap[sy][sx] = 1
                length += 1
                sx += 1

            if sx < N:
                for _sx in range(sx - 1, core_x, -1):
                    maap[sy][_sx] = 0
                    length -= 1
                go(node + 1, maap, length, cnt)
            else:
                go(node + 1, maap, length, cnt + 1)
                for _sx in range(sx - 1, core_x, -1):
                    maap[sy][_sx] = 0
                    length -= 1




T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    position = []
    for i in range(N):
        for j in range(N):
            if maap[i][j] == 1 and not (i == 0 or i == N-1 or j == 0 or j == N-1):
                position.append((i, j))
    num_nodes = len(position)
    #print('num _nodes : ',position)
    results = (-1, 9999)
    go(0, maap, 0, 0)
    #results.sort(key=lambda x:x[0], reverse=True)

    print('#{} {}'.format(tc, results[1]))

