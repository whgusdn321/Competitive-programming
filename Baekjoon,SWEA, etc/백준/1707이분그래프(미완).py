import sys
from collections import deque
read = lambda :sys.stdin.readline().rstrip()

test_cases = int(read())


# def go(i, arr, visited, before_color, color):
#     if color[i] == -1:
#         color[i] = 1-before_color
#         for child in arr[i]:
#             if visited[child] < 2:
#                 visited[child] += 1
#                 before_color = 1-before_color
#                 go(child, arr, visited, before_color, color.copy())
#     else:
#         if color[i] == before_color:
#             print('NO')
#             sys.exit()
#         else:
#             for child in arr[i]:
#                 if visited[child] < 2:
#                     visited[child] += 1
#                     before_color = 1-before_color
#                     go(child, arr, visited, before_color, color.copy())


def inspect(arr, color):
    temp = arr.popleft()
    color[temp[0]] = 0
    color[temp[1]] = 1
    queue = arr
    while queue:
        temp = queue.popleft()
        if color[temp[0]] == -1 and color[temp[1]] == -1:
            queue.append(temp)
        elif color[temp[0]] != -1 and color[temp[1]] == -1:
            color[temp[1]] = 1 - color[temp[0]]
        elif color[temp[0]] == -1 and color[temp[1]] != -1:
            color[temp[0]] = 1 - color[temp[1]]
        else:
            if color[temp[0]] == color[temp[1]]:
                print('NO')
                return
    print("YES")
    return


def elem(ele):
    return ele[0]


for test_case in range(test_cases):
    V, E = map(int, read().split())
    arr= []
    for _ in range(E):
        a, b = map(int, read().split())
        arr.append([a, b])
    arr.sort(key = elem)
    arr = deque(arr)
    color = [-1] * (V+1)
    inspect(arr, color)



