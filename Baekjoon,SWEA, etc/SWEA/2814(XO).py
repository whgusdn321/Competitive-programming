"""
bactracking 문제.
내가 backtracking 문제를 풀며 항상 햇깔리는것은 뭐냐하면, 바로 visited와 관련해서 return할때 언제 False로 만들어줄지.. 또 어떻게 True로 만들어 준뒤 함수를 call할것인지..
그런것이 햇깔린다.

현재까지 내가 알아낸 Backtracking은 그래서 총 2가지 유형이 있다.
첫번째. 가서 visited를 True로 만든다.
두번째. 들어가기전 visited를 True로 만든다.

첫번째는 왠만해서 거의 모든 Backtracking 알고리즘에 다 쓰일 수 있는것 같고,
두번째는 알고리즘의 코드가 보기 편하다. 하지만 안되는 경우가 있다. 예를 들어, Nqueen 문제, 또 SWEA 1798같은 문제..
왜 안되는가? 두문제 전부 먼저 visited 를 체크하고 나면, promising 을 채크하는 부분에서 걸리기 때문이다..
"""


def go(node, graph, cnt):

    global visited, cnts

    if visited[node]:
        cnts.append(cnt)
        return
    else:
        cnt += 1
        visited[node] = True
        for child in graph[node]:
            go(child, graph, cnt)
        visited[node] = False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnts = []
    visited = [False] * (N+1)
    for vertex in range(1, N+1):
        cnt = 0
        go(vertex, graph, cnt)
        cnts.append(cnt)
    if M == 0:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, max(cnts)))
