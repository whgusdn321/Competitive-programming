import sys
sys.setrecursionlimit(1000000000)
read = lambda :sys.stdin.readline().rstrip()

N, M = map(int, read().split())
arr = [int(a) for a in read().split()]
arr.sort()


def go(arr, stack):
    if len(stack) == M:
        for item in stack:
            print(item, end=' ')
        print()
        return
    else:
        for i in range(len(arr)):
            if not stack:
                stack.append(arr[i])
                go(arr, stack)
                stack.pop()
            else:
                if arr[i] >= stack[-1]:
                    stack.append(arr[i])
                    go(arr, stack)
                    stack.pop()

go(arr, [])