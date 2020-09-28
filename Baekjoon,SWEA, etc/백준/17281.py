from collections import deque


def simulate(permu, N, arrs):
    points = 0
    i = 0
    q = deque([])
    for _ in range(3):
        q.append(0)
    for n in range(N):
        arr = arrs[n]
        #q = queue.Queue()
        if n != 0:
            for _ in range(3):
                q.popleft()
                q.append(0)
        out = 0
        while out < 3:
            hitter = permu[i]
            if arr[hitter] == 0:
                out += 1
            elif arr[hitter] == 1:
                points += q.popleft()
                q.append(1)
            elif arr[hitter] == 2:
                points += q.popleft()
                q.append(1)
                points += q.popleft()
                q.append(0)
            elif arr[hitter] == 3:
                points += q.popleft()
                q.append(1)
                points += q.popleft()
                q.append(0)
                points += q.popleft()
                q.append(0)
            else:  # arr[hitter] == 4
                points += q.popleft()
                q.append(1)
                points += q.popleft()
                q.append(0)
                points += q.popleft()
                q.append(0)
                points += q.popleft()
                q.append(0)
            i = (i+1)%len(arr)
    return points


def make_permus(depth, stakk):
    global permus
    if depth == 9:
        permus.append(stakk.copy())
        return
    elif depth == 3:
        stakk.append(0)
        make_permus(depth+1, stakk)
        stakk.pop()
    else:
        for n in [1,2,3,4,5,6,7,8]:
            if n not in stakk:
                stakk.append(n)
                make_permus(depth+1, stakk)
                stakk.pop()

N = int(input())
arrs = []
for _ in range(N):
    arr = [int(char) for char in input().split()]
    arrs.append(arr)
permus = []
make_permus(0, [])
#print(len(permus))
# boool = True
# for i in range(len(arrs)-1):
#     if arrs[i] == arrs[i+1]:
#         boool &= True
#     else:
#         boool &= False
# if boool:
#     permus = [permus[0]]
#     #print('hi!')
results = 0
for permu in permus:
    point = simulate(permu, N, arrs)
    if point > results:
        results = point
print(results)
#print('permus : ', permus)
#print(len(permus))
