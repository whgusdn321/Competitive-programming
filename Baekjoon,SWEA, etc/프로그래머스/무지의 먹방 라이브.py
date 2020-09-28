from collections import defaultdict, deque


def solution(food_times, k):
    N = len(food_times)
    tmpdict = defaultdict(int)
    for food in food_times:
        tmpdict[food] += 1
    listt = []
    for key, val in tmpdict.items():
        listt.append((key, val))
    listt.sort()

    dq = deque(listt)
    len_arr = len(food_times)
    visited = defaultdict(bool)

    l = 0
    while dq and k >= len_arr * (dq[0][0]-l):
        k -= (len_arr * (dq[0][0]-l))
        len_arr -= dq[0][1]
        visited[dq[0][0]] = True
        l = dq[0][0]
        dq.popleft()

    if not dq:
        return -1
    else:
        k %= len_arr
        ans = -1
        cnt = 0
        for i in range(N):
            if visited[food_times[i]]:
                continue
            else:
                if cnt == k:
                    ans = i
                    break
                else:
                    cnt += 1
        return ans+1