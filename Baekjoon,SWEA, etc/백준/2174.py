import sys
from collections import deque
W, H = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())
#N = robots, #M = commands
robots = [[None, None, None] for _ in range(101)]
commands = []
maap = [[0]*(W+1) for _ in range(H+1)]

for i in range(N):
    robot_temp = sys.stdin.readline().split()
    robots[i+1][0] = int(robot_temp[0])#x
    robots[i+1][1] = int(robot_temp[1])#y
    robots[i+1][2] = robot_temp[2]
    maap[int(robot_temp[1])][int(robot_temp[0])] = i+1

for _ in range(M):
    com_temp = sys.stdin.readline().split()
    n = int(com_temp[2])
    for __ in range(n):
        commands.append([int(com_temp[0]), com_temp[1]])

commands = deque(commands)
#print('commands : ',commands)
Flag = False
while(commands):
    r, com = commands.popleft()
    robot = robots[r]
    if com == 'F':
        cur_x, cur_y, dir = robot[0], robot[1], robot[2]
        if dir == 'E':
            next_y, next_x = cur_y, cur_x+1
        elif dir == 'N':
            next_y, next_x = cur_y+1, cur_x
        elif dir == 'W':
            next_y, next_x = cur_y, cur_x-1
        else:
            next_y, next_x = cur_y-1, cur_x

        if 0<next_y<=H and 0<next_x<=W:
            if maap[next_y][next_x] != 0:
                print("Robot {} crashes into robot {}".format(r, maap[next_y][next_x]))
                Flag = True
                break
            else:
                maap[cur_y][cur_x] = 0
                maap[next_y][next_x] = r
                robots[r][0] = next_x
                robots[r][1] = next_y
        else:
            print('Robot {} crashes into the wall'.format(r))
            Flag = True
            break
    elif com == 'R':
        dir = robot[2]
        if dir == 'E':
            next_dir = 'S'
        elif dir == 'S':
            next_dir = 'W'
        elif dir == 'W':
            next_dir = 'N'
        else:
            next_dir = 'E'
        robot[2] = next_dir

    else:
        dir = robot[2]
        if dir == 'E':
            next_dir = 'N'
        elif dir == 'S':
            next_dir = 'E'
        elif dir == 'W':
            next_dir = 'S'
        else:
            next_dir = 'W'
        robot[2] = next_dir
if not Flag:
    print('OK')