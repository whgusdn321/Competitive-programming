import sys
read = lambda: sys.stdin.readline()
from copy import deepcopy
N = int(read())
map = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    map.append(temp)

#상 : 0, 하 :1, 좌 : 2, 우 : 3
def permu(stack):
    global visited, stacks
    if len(stack) == 5:
        stacks.append(stack.copy())
        return
    for i in range(4):
        stack.append(i)
        permu(stack)
        stack.pop()

stacks = []
permu([])
#print('stacks : ',len(stacks))


def left(arr):
    for i in range(0, len(arr)):
        if arr[i] == 0:
            continue
        j = i-1
        while j>=0 and arr[j] == 0: # arr[i]가 0 이 아닐때, arr에서
            j -= 1
        if j == i-1:
            arr[j+1] = arr[i]
        else:
            arr[j+1] = arr[i]
            arr[i] = 0

arrr= [1,0,3, 0, 5]
left(arrr)
print('arrr: ',arrr)


max_blocks = []
#상 : 0, 하 :1, 좌 : 2, 우 : 3
for permu in stacks: #0, 0, 0, 0, 0
    maap = deepcopy(map)
    for oper in permu:
        if oper == 2:
            for i in range(N):
                arr = maap[i]
                left(arr)
                for j in range(0, N-1):
                    if arr[j] == arr[j+1]:
                        arr[j] *= 2
                        arr[j+1] = 0
                        left(arr)
        if oper == 3:
            for i in range(N):
                temp = maap[i]
                arr2 = []
                for j in range(len(temp)-1, -1, -1):
                    arr2.append(temp[j])
                left(arr2)
                for j in range(0, N - 1):
                    if arr2[j] == arr2[j + 1]:
                        arr2[j] *= 2
                        arr2[j + 1] = 0
                        left(arr2)
                for i, item in enumerate(arr2):
                    temp[-(i+1)] = item
        if oper == 0:
            for i in range(N):
                arr3 = []
                for j in range(N):
                    arr3.append(maap[j][i])
                #1개의 행 완성
                left(arr3)
                for j in range(0, N - 1):
                    if arr3[j] == arr3[j + 1]:
                        arr3[j] *= 2
                        arr3[j + 1] = 0
                        left(arr3)
                for j, item in enumerate(arr3):
                    maap[j][i] = item

        if oper == 1:
            for i in range(N):
                arr4 = []
                for j in range(-1, -N-1, -1):
                    arr4.append(maap[j][i])
                #1개의 행 완성
                left(arr4)
                for j in range(0, N - 1):
                    if arr4[j] == arr4[j + 1]:
                        arr4[j] *= 2
                        arr4[j + 1] = 0
                        left(arr4)
                for j, item in enumerate(arr4):
                    maap[-(j+1)][i] = item
    max_i =0
    max_j = 0
    for y in range(N):
        for x in range(N):
            if maap[y][x] > maap[max_i][max_j]:
                max_i = y
                max_j = x
    max_blocks.append(maap[max_i][max_j])
print(max(max_blocks))