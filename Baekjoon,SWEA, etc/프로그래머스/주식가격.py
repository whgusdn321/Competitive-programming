from collections import deque


def solution(prices):
    n = len(prices)
    arr = [1]*n
    arr[-1] = 0
    for i in range(n-2, -1, -1):
        idx = i + arr[i]
        while prices[i] <= prices[idx] and idx < n-1:
            idx += arr[idx]
        arr[i] = idx-i
    print(arr)
    return arr
solution([1,2,3,1,2])