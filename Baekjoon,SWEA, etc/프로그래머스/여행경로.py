from collections import defaultdict
graph = None
visited = None
answer = None


def go(ffrom, depth, result):
    global answer, graph
    answer.append(ffrom)
    for i, togo in enumerate(graph[ffrom]):
        if not visited[ffrom][i]:
            visited[ffrom][i] = True
            go(togo)


def solution(tickets):
    global graph, visited, answer
    graph = defaultdict(list)
    visited = defaultdict(list)

    for ffrom, togo in tickets:
        graph[ffrom].append(togo)
        visited[ffrom].append(False)
    for key, arr in graph.items():
        arr.sort() # sort the array
    # print('graph : ', graph)
    # print('visited : ',visited)
    answer = []
    go('ICN')
    return answer

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))