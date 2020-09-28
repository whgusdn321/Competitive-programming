def go(i, summ):
    global graph, t, p, results
    results.append(summ)
    for child in graph[i]:
        go(child, summ+p[child])


N = int(input())
t = []
p = []
for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
invalids = []
for i in range(N):
    if t[i] > N - i:
        invalids.append(i)
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+t[i], N):
        if j not in invalids:
            graph[i].append(j)
results = []
for i in range(N):
    if i not in invalids:
        go(i, p[i])
if results:
    print(max(results))
else:
    print(0)

