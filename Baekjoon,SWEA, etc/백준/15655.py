import sys
read = lambda :sys.stdin.readline().rstrip()

N, M = map(int, read().split())
arr = [int(a) for a in read().split()]
arr.sort()


def go(i, arr, stack):
    global M, visited
    if len(stack) == M:
        for item in stack:
            print(item, end=' ')
        print()
    else:
        for j in range(i+1, len(arr)):
            if not visited[j]:
                visited[j] = True
                stack.append(arr[j])
                go(j, arr, stack)
                stack.pop()
                visited[j] = False


visited= [False] * N
go(-1, arr, [])