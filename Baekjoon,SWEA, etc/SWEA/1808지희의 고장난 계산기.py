import queue
def go(before, current, mode, cnt):
    global availables, wanted, results
    # print('before : ',before)
    # print('current : ',current)
    # print('mode : ',mode)
    # print()
    if before * current > wanted:
        return
    if mode == 'normal':
        for allowed in availables:
            if not (current == 0 and allowed == 0):
                go(before, current*10 + allowed, 'normal', cnt+1)
        if current != 1 and current != 0:
            go(before, current, 'mul', cnt+1)
    else:
        before *= current
        if before == wanted:
            results.append(cnt)
            return
        else:
            go(before, 0, 'normal', cnt)


def bfs(available, wanted):
    q = queue.Queue()
    visited = [False] * (10**6+1)
    ans = -1
    q.put([1, 0, 0, 'normal'])  # before, current, cnt, mode
    while q.qsize() != 0:
        before, cur, cnt, mode = q.get()
        if mode == 'normal':
            if before * cur > wanted:
                continue
            visited[before] = True
            for ava in available:
                if before != 0 or ava != 0:
                    q.put([before, cur*10+ava, cnt + 1, 'normal'])
            if cur != 0 and cur != 1:
                q.put([before, cur, cnt+1, 'mul'])
        else:  # mode == 'mul'
            before *= cur
            if before == wanted:
                ans = cnt
                break
            else:
                if not visited[before]:
                    q.put([before, 0, cnt, 'normal'])

    return ans


def length(num):
    cnt = 0
    while num != 0:
        cnt += 1
        cnt //= 10
    return cnt


def inspect(next_num, availables):
    temps = []
    while next_num != 0:
        temp = next_num %10
        temps.append(temp)
        next_num //= 10

    for item in temps:
        if item not in availables:
            return False
    return True


def bfs2(wanted, availables):
    ans = []
    q = queue.Queue()
    q.put([wanted, 0])

    while q.qsize() != 0:
        num, cnt = q.get()
        print('num : ')
        for ava in availables:
            if ava != 1 and ava != 0 and num % ava == 0:
                next_num = num // ava
                next_cnt = cnt + 2
                if inspect(next_num, availables):
                    ans.append(next_cnt+length(next_num)+1)
                else:
                    q.put([next_num, next_cnt])
    if ans:
        return min(ans)
    else:
        return -1

T = int(input())
for tc in range(1, T+1):
    temp = [int(char) for char in input().split()]
    availables = [i for i in range(10) if temp[i]]
    wanted = int(input())
    #print('wanted : ',wanted)
    #print('av',availables)

    ans = bfs(availables, wanted)
    #ans = bfs2(wanted, availables)
    print('#{} {}'.format(tc, ans))



    # results = []
    # go(1, 0, 'normal', 0)
    # if results :
    #     print('#{} {}'.format(tc ,min(results)))
    # else:
    #     print('#{} {}'.format(tc , -1))
    #queue = deque([(item, 1, 'normal') for item in availables])
