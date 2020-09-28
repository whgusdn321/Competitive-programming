import sys
from collections import deque

read = lambda:sys.stdin.readline().rstrip()
gear1 = deque([int(a) for a in read()])
gear2 = deque([int(a) for a in read()])
gear3 = deque([int(a) for a in read()])
gear4 = deque([int(a) for a in read()])
gears = [gear1, gear2, gear3, gear4]

test_cases = int(read())

for test_case in range(test_cases):
    n_gear, dirr = map(int, read().split())
    n_gear -= 1 # 0<=n_gear-1<=3
    i = n_gear-1
    j = n_gear+1
    mv_gears = [[n_gear, dirr]]

    dir = dirr

    while i>=0:
        if gears[i][2] != gears[i+1][-2]:
            mv_gears.append([i, -dir])
            dir = -dir
        else:
            break
        i -= 1
    dir = dirr

    while j<len(gears):
        if gears[j][-2] != gears[j-1][2]:
            mv_gears.append([j, -dir])
            dir = -dir
        else:
            break
        j += 1

    # print('moving _gears : ', mv_gears)
    for _ in range(len(mv_gears)):
        index, dirrr = mv_gears.pop()
        gear = gears[index]
        if dirrr == 1:
            a = gear.pop()
            gear.appendleft(a)
        else:
            a = gear.popleft()
            gear.append(a)
    # print('gears : ')
    # for _ in range(len(gears)):
    #     print(gears[_])

sum = 0
if gears[0][0] == 1:
    sum += 1
if gears[1][0] == 1:
    sum += 2
if gears[2][0] == 1:
    sum += 4
if gears[3][0] == 1:
    sum += 8
print(sum)




