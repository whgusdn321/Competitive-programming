import itertools
from copy import deepcopy

"""
약간의 응용이 필요한, 복잡한 완전탐색 문재라고 생각하였다.
처음에 만들었을때, Test cases들은 전부 맞았지만, 제출했더니 시간초과가 떴다.
아마 deepcopy 때문일것이라고 예측하고, deepcopy부분을 없애주었다.
약 20x20의 maap에서 3차원 이상의 for문 안에서 deepcopy를 사용하면 시간초과가 날 확률이 높다.
아무튼 deepcopy를 문제를 푸는데 먼저 활용하고, 마지막 시간이 남으면 없애준다는 생각을 꼭 가져야 한다.
 
"""
def _check(arr, K):
    temp = []
    cnt = 1
    for i in range(0, len(arr)):
        if i == len(arr) - 1:
            temp.append(cnt)
            break
        if arr[i] == arr[i+1]:
            cnt += 1
            continue
        else:
            temp.append(cnt)
            cnt = 1
    if max(temp) >= K:
        return True
    else:
        return False


def check(maap, K):
    global H, W
    for x in range(W):
        arr = [maap[i][x] for i in range(H)]
        if not _check(arr, K):
            return False
    return True


def generateAB(N, stack):
    '''
    If combi is [1,2], This function creates [0, 0], [0, 1], [1, 0], [1, 1] (possible products of 1,0)
    param N: length of combi
    param stack: stack that has possible products that will append to ABs(global)
    return: None
    '''
    global ABs
    if len(stack) == N:
        ABs.append(stack.copy())
    else:
        stack.append(0)
        generateAB(N, stack)
        stack.pop()
        stack.append(1)
        generateAB(N, stack)
        stack.pop()

test_cases = int(input())

for test_case in range(1, test_cases+1):
    H, W, K = map(int, input().split())
    maap = []
    for _ in range(H):
        temp = [int(a) for a in input().split()]
        maap.append(temp)

    if check(maap, K):
        #print('checkmate')
        result = 0
        print('#{} {}'.format(test_case, result))
    else:
        rows = [i for i in range(H)]
        result = 0

        for k in range(1, H+1):
            combis = itertools.combinations(rows, k) #combis = [[0],[1],[2],[3],[4], [0,1], [0,2]] ...
            boool = False

            for combi in combis:
                # 각각의 combi에 해당하는 row들을
                # generateAB에 의해서 만들어진 ABs의 원소 [0, 0] 이면 row[0]는 전부
                ABs = []
                generateAB(len(combi), [])
                k = len(combi)
                for abs in ABs:
                    temp = []
                    for i in range(k):
                        if abs[i] == 0:
                            temp.append(maap[combi[i]])
                            maap[combi[i]] = [0] * W
                        else:
                            temp.append(maap[combi[i]])
                            maap[combi[i]] = [1] * W
                    if check(maap, K):
                        boool = True
                        for i in range(k): #맵 원상복귀
                            maap[combi[i]] = temp[i]
                        break
                    for i in range(k): # 맵 원상복귀
                        maap[combi[i]] = temp[i]
                if boool:
                    result = k
                    break
            if boool:
                break
        print('#{} {}'.format(test_case, result))




