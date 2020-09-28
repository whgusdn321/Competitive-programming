import sys
read = lambda :sys.stdin.readline()
N = int(read())

arr = [0] *(N+1)
visited = [False] *(N+1)
real_stack = []

for i in range(1, N+1):
    a = int(read())
    arr[i] = a


def go(i, visited):
    global arr
    visited[i] = True
    stack =[i]
    l = i
    while not visited[arr[l]]:
        visited[arr[l]] = True
        l = arr[l]
        stack.append(l)

    if arr[l] == i:
        #print('stack L ',stack)
        return stack
    else:
        for item in stack:
            visited[item] = False
        visited[i] = False
        return -1


for i in range(1, N+1):
    if not visited[i]:
        stackk = go(i, visited)
        if stackk != -1:
            for item in stackk:
                real_stack.append(item)

real_stack.sort()
print(len(real_stack))
for item in real_stack:
    print(item)

