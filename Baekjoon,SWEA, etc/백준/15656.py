import sys
sys.setrecursionlimit(1000000000)
read = lambda :sys.stdin.readline().rstrip()

N, M = map(int, read().split())
arr = [int(a) for a in read().split()]
arr.sort()


def go(arr, stack):
    if len(stack) == M:
        for a in stack:
            print(a, end=' ')
        print()
        return
    for i in range(len(arr)):
            stack.append(arr[i])
            go(arr, stack)
            stack.pop()



visited = [False]*N
go(arr, [])

