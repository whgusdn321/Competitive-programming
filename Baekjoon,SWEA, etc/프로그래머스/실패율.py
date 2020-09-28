from collections import defaultdict


def solution(N, stages):
    stages.sort()
    dict1 = defaultdict(int)
    n = len(stages)
    for stage in stages:
        dict1[stage] += 1
    # list1 = sorted(dict1, key=lambda x:x[0])
    rets = []
    for i in range(1, N+1):
        if n == 0:
            rets.append((i, 0))
        else:
            rets.append((i, dict1[i]/n))
            n -= dict1[i]
    print(rets)
    rets.sort(key=lambda x:-x[1])
    print(rets)
    ans = []
    for x, _ in rets:
        ans.append(x)
    return ans

print(solution(4, [4,4,4,4,4] ))