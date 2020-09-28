from collections import deque


def update_state(gears, state):
    state[0][1] = gears[0][2]
    state[1][0] = gears[1][6]
    state[1][1] = gears[1][2]
    state[2][0] = gears[2][6]
    state[2][1] = gears[2][2]
    state[3][0] = gears[3][6]


def rotate(gear, dir):
    if dir == 1:
        t = gear.pop()
        gear.appendleft(t)
    else:
        t = gear.popleft()
        gear.append(t)


gears = []
opers = []

for _ in range(4):
    gear = [int(char) for char in input()]
    gears.append(deque(gear))

nopers = int(input())
for _ in range(nopers):
    temp = [int(char) for char in input().split()]
    opers.append(temp)

opers = deque(opers)
state = [[None, None] for _ in range(4)]
update_state(gears, state)

while opers:
    stack1 = []
    stack2 = []
    oper = opers.popleft()
    n = oper[0] - 1
    dir = oper[1]
    l = n - 1
    r = n + 1
    while l >= 0 and state[l][1] != state[l+1][0]:
        stack1.append(l)
        l -= 1

    while r < 4 and state[r][0] != state[r-1][1]:
        stack2.append(r)
        r += 1

    rotate(gears[n], dir)
    cnt = 1

    for n in stack1:
        if cnt % 2 == 1:
            rotate(gears[n], -dir)
            cnt += 1
        else:
            rotate(gears[n], dir)
            cnt += 1
    cnt = 1
    for n in stack2:
        if cnt % 2 == 1:
            rotate(gears[n], -dir)
            cnt += 1
        else:
            rotate(gears[n], dir)
            cnt += 1
    update_state(gears, state)
print(1*gears[0][0] + 2*gears[1][0] + 4*gears[2][0] + 8*gears[3][0])