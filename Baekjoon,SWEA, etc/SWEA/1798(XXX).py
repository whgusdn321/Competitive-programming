def go(time, day, visited, node, score, history):
    global adj_mtx, vertexes, travelscore, traveltime, results,\
            N, M, scores

    ## 종료조건들
    if day > M:
        return
    if time > 540: #invalid time
        return
    if vertexes[node] == 'P' and visited[node]:
        return
    if vertexes[node] == 'A':
        if visited[node] and day == M:
            if not results:
                results.append((score, history.copy()))
            else:
                if results[0][0] < score:
                    results.pop()
                    results.append((score, history.copy()))
            return
        else:
            if visited[node]:
                return

    history.append(node)
    visited[node] = True
    
    if vertexes[node] == 'H':
        if time > 500:
            time = 0
        day += 1

    if vertexes[node] == 'P':
        time += traveltime[node]
        score += travelscore[node]

    for child in range(1, N+1):
        if adj_mtx[node][child] != 0: #if valid child
            go(time + adj_mtx[node][child], day, visited, child, score, history)
    visited[node] = False
    history.pop()


testcases = int(input())

for T in range(1, 1+testcases):
    N, M = map(int, input().split())
    adj_mtx = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N):
        info = [int(time) for time in input().split()] #1 -> 9, 2->8 ...
        k = 0
        for j in range(i+1, N+1):
            adj_mtx[i][j] = info[k]
            k += 1
    for i in range(1, N+1):
        for j in range(1, i):
            adj_mtx[i][j] = adj_mtx[j][i]


    vertexes = {}
    hotel = []
    travel = []
    travelscore = [0] * (N+1)
    traveltime = [0] * (N+1)
    airport = []
    scores = [0] * (N+1)#scores[i][j] 하면, history가 i length이고 j 는 그때의 노드의 최댓값이라고 하자.
    for i in range(1, N+1):
        info = [char for char in input().split()]
        if info[0] == 'A':
            vertexes[i] = 'A'
        elif info[0] == 'P':
            vertexes[i] = 'P'
            traveltime[i] = int(info[1])
            travelscore[i] = int(info[2])
        else:
            vertexes[i] = 'H'

    results = []
    visited = [False] * (N+1)
    go(0, 1, visited, 1, 0, [])



    if results:
        history = results[0][1]
        score = results[0][0]
        temp = history.pop(0)
        history.append(temp)
        print('#{} {}'.format(T, score), end= ' ')
        for item in history:
            print(item, end=' ')
        print()
    else:
        print('#{} {}'.format(T, 0))
