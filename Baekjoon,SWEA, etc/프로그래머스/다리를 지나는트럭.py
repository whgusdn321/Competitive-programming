from collections import deque

"""
수도 없는 실수, 시행착오..
진짜 역대급으로 실수 많이 한 문제가 이문제다..
풀어놓고도 말이 안나온다.. 
"""


def solution(bridge_length, weight, truck_weights):
    N = bridge_length
    time = 0
    limit = weight
    trucks = deque(truck_weights)

    summ = 0
    cnt = 0
    bridge = deque([])

    while 1:
        while trucks and summ + trucks[0] <= limit and cnt < N:
            truck = trucks.popleft()
            bridge.append(truck)
            cnt += 1
            summ += truck
            time += 1
        time += (N - cnt)
        tt = cnt
        boool = False
        for _ in range(tt): # make next bridge
            if not bridge:
                break
            trash = bridge.popleft()
            summ -= trash

            cnt -= 1
            time += 1
            if trucks and summ + trucks[0] <= limit:
                truck = trucks.popleft()
                bridge.append(truck)
                summ += truck
                cnt += 1
                boool = True
            elif boool:
                if trucks:
                    bridge.append(0)
                cnt += 1

        if not bridge and not trucks:
            break

    return time






def solution2(bridge_length, weight, truck_weights):
    a = [0 for _ in range(bridge_length)]
    n = len(truck_weights)
    k = deque(truck_weights)
    step = 0
    finished = []
    sum_a = 0
    while (len(finished) != n):
        # a 는 bridge_length만큼의 list이다. 초기에 전부 0을 가지고 있다.
        step += 1
        if len(k) == 0:
            for i in range(bridge_length):
                if a[i] != 0:
                    if i != 0:
                        a[i - 1] = a[i]
                        a[i] = 0
                    else:
                        sum_a -= a[i]
                        a[i] = a[i + 1]
                        finished.append(0)

                        # a[i] = 0
            continue
        if (sum_a + k[0]) > weight:
            for i in range(bridge_length):
                if a[i] != 0:
                    if i != 0:
                        a[i - 1] = a[i]
                        a[i] = 0
                    else:
                        sum_a -= a[i]
                        a[i] = a[i + 1]
                        finished.append(0)
                        # a[i+1] = 0
            if (sum_a + k[0]) <= weight:
                a[bridge_length - 1] = k[0]
                sum_a += k[0]
                k.popleft()
            continue
        if (sum_a + k[0]) <= weight:  # 다리에 있는 트럭들의 무게의 합과 대기열의 첫번째 트럭의 합이 weight보다 같거나 작을때
            for i in range(bridge_length):
                if a[i] != 0:
                    if i != 0:
                        a[i - 1] = a[i]
                        a[i] = 0
                    else:
                        sum_a -= a[i]
                        a[i] = a[i + 1]
                        finished.append(0)
                        # a[i+1] = 0
            a[bridge_length - 1] = k[0]
            sum_a += k[0]
            temp = k.popleft()

    answer = step
    return answer

print(solution(4, 14, [3,1, 6, 7, 9]))
print(solution2(4, 14, [3,1, 6, 7, 9]))