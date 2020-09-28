import itertools
def compare(elem):
    return elem[2]


def solution(n, costs):
    """
    :param n: 4
    :param costs: [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    :return: 4
    """
    costs.sort(key=compare)
    results = []
    for combi in itertools.combinations(costs, n-1):
        print('combi : ',combi)
        track = set([])
        summ = 0
        for bridge in combi:
            track.add(bridge[0])
            track.add(bridge[1])
            summ += bridge[2]
        if len(track) == n:
            results.append(summ)
    print('results : ', results)
    return min(results)
    # track = set([])
    # summ = 0
    # sides = 0
    # for i in range(len(costs)):
    #     if sides == n - 1:
    #         break
    #     if not ((costs[i][0] in track) and (costs[i][1] in track)):
    #         summ += costs[i][2]
    #         track.add(costs[i][0])
    #         track.add(costs[i][1])
    #         sides += 1
    #
    # return summ
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))