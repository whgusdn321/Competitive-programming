from collections import deque


def inspect(co, br):
    for item in br:
        if item == co:
            return True
    return False


c, b = map(int, input().split())
cony = c
brown = deque([b])

time = 0
boool = False
while 1:
    if inspect(cony, brown):
        boool = True
        break
    time += 1
    cony += time
    if not 0<=cony<=200000:
        break
    for i in range(len(brown)):
        a = brown.popleft()
        nb1 = a-1
        nb2 = a+1
        nb3 = a*2
        if 0 <= nb1 <= 200000:
            brown.append(nb1)
        if 0 <= nb2 <= 200000:
            brown.append(nb2)
        if 0 <= nb3 <= 200000:
            brown.append(nb3)
if boool:
    print(time)
else:
    print(-1)