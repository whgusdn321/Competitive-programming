from itertools import permutations

visited = None


def solution(n, weak, dist):
    global visited
    visited = [False] * len(weak)
    ans = 10**9
    for _ in range(len(weak) -1):
        for p_size in range(1, len(dist)+1):
            for permu in permutations(dist, p_size):
                for i in range(len(visited)):  # init visited
                    visited[i] = False
                p = 0
                cnt = 0
                for i in range(len(weak)):
                    if not visited[i]:
                        if p >= len(permu):
                            break
                        j = i
                        while j < len(weak):
                            dis = weak[j] - weak[i]
                            if dis <= permu[p]:
                                visited[j] = True
                                j += 1
                                cnt += 1
                            else:
                                break
                        p += 1
                    else:
                        continue
                if cnt == len(weak):
                    ans = min(ans, p)

        tmp = weak.pop(0)
        weak.append(tmp+n)
    if ans == 10**9:
        return -1
    else:
        return ans

    # for p_size in range(1, len(dist)+1):
    #     for permu in permutations(dist, p_size):
    #         for i in range(len(visited)):  # init visited
    #             visited[i] = False
    #         p = 0
    #         cnt = 0
    #         for i in range(len(weak)):
    #             if not visited[i]:
    #                 if p >= len(permu):
    #                     break
    #                 j = i
    #                 while j < len(weak):
    #                     dis = weak[j] - weak[i]
    #                     if dis <= permu[p]:
    #                         visited[j] = True
    #                         j += 1
    #                         cnt += 1
    #                     else:
    #                         break
    #                 p += 1
    #             else:
    #                 continue
    #         if cnt == len(weak):
    #             ans = min(ans, p)
    # if ans == 10**9:
    #     return -1
    # else:
    #     return ans

print(solution(12, [1,3,4,9,10],[3,5,7]))