def go(node, day, timespent, summ, stakk):
    global days, visited, results, points, hotels, airports, po_dict, N, children

    if day > days or timespent > 540:
        return

    if node in points:
        timespent += po_dict[node][0]
        summ += po_dict[node][1]
        visited[node] = True
        stakk.append(node)
        if timespent > 540:
            stakk.pop()
            visited[node] = False
            return
        else:
            for child in children:
                if graph[node][child] != 0:
                    go(child, day, timespent+graph[node][child], summ, stakk)
            visited[node] = False
            stakk.pop()
    elif node in hotels:
        stakk.append(node)
        for child in points:
            if graph[node][child] != 0 and not visited[child]:
                #go(child, day, timespent+graph[node][child], summ, stakk)
                go(child, day+1, graph[node][child], summ, stakk)
        stakk.pop()
    else:  # node in Airports
        stakk.append(node)
        if day == days:
            results.append([summ, stakk.copy()])
            stakk.pop()
            return
        else:
            for child in points:
                if graph[node][child] != 0 and not visited[child]:
                    go(child, day, timespent+graph[node][child], summ, stakk)
            stakk.pop()


T = int(input())
for tc in range(1, T+1):
    N, days = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    children = [i for i in range(1, N+1)]
    visited = [False]*(N+1)
    for i in range(1, N):
        row = [int(char) for char in input().split()]
        for j in range(i+1, 1+N):
            graph[i][j] = row[j-i-1]
            graph[j][i] = row[j-i-1]
    # for _ in range(N+1):
    #     print(graph[_])
    hotels = []
    airports = []
    points = []
    po_dict = {}
    for n in range(1, N+1):
        string = input().split()
        if string[0] == 'A':
            airports.append(n)
        elif string[0] =='H':
            hotels.append(n)
        else:
            points.append(n)
            po_dict[n] = (int(string[1]), int(string[2]))
    # print('hotels : ',hotels)
    # print('airports : ',airports)
    # print('points : ',points)
    results = []
    go(1, 1, 0, 0, [])
    results.sort(key = lambda x:x[0], reverse=1)
    print('results : ', results[0])