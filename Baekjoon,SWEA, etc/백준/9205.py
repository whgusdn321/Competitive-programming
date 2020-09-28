import sys
read = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000000)

test_cases = int(read())

for _ in range(test_cases):
    n = int(read())
    home = [int(a) for a in read().split()]


    def go(y, x):
        global visited, points
        visited.append((y, x))
        boool = False
        if y == goal[0] and x == goal[1]:
            return True
        for point in points:
            manhattan = abs(y - point[0]) + abs(x - point[1])
            if manhattan <= 1000 and point not in visited:
                boool |= go(point[0], point[1])
        return boool




    points = []
    for _ in range(n+1):
        a, b = map(int , read().split())
        points.append((a, b))

    visited = []
    goal = (points[-1][0], points[-1][1])
    boool = go(home[0], home[1])

    if boool:
        print('happy')
    else:
        print('sad')
