T = 10
for tc in range(1, T+1):
    _ = input()
    maap = []
    for _ in range(100):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    arr = maap[0]
    sxs = []
    wanted_x = 0
    for i in range(100):
        if arr[i] == 1:
            sxs.append(i)
    arr = maap[99]
    for i in range(100):
        if arr[i] == 2:
            wanted_x = i
    boool = False
    for sxx in sxs:
        sy, sx, sdir = 0, sxx, 'S'
        while sy != 99:
            if sdir == 'S':
                if sx+1<100 and maap[sy][sx+1] == 1:
                    sx += 1
                    sdir = 'E'
                    continue
                elif sx-1>=0 and maap[sy][sx-1] == 1:
                    sx -= 1
                    sdir = 'W'
                    continue
                else:
                    sy += 1
                    continue
            elif sdir == 'E':
                if maap[sy+1][sx] == 1:
                    sy += 1
                    sdir = 'S'
                    continue
                else:
                    sx += 1
                    continue
            else:
                if maap[sy+1][sx] == 1:
                    sy += 1
                    sdir = 'S'
                    continue
                else:
                    sx -= 1
                    continue
        if sx == wanted_x:
            print('#{} {}'.format(tc, sxx))
            break
