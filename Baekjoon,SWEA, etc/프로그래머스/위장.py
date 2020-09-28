

def go(i, depth, limit, result):
    global arr, N, results
    if depth == limit:
        results += result
    for j in range(i+1, N):
        go(j, depth+1, limit, result * arr[j])


arr= [3]
N = len(arr)
results = 0


for n in range(1, len(arr)+1):
    go(-1, 0, n, 1)
print(results)


"""
import itertools
from collections import defaultdict
def solution(clothes):
    dictionary = defaultdict(int)
    answer = 0
    for cloth1, kind in clothes:
        dictionary[kind] += 1
    arr = []
    for key, item in dictionary.items():
        arr.append(item)
    for i in range(1, len(arr)+1):
        a = itertools.combinations(arr, i)
        for combi in a:
            product = 1
            for item in combi:
                product *= item
            answer += product
    return answer
"""