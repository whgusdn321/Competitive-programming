from collections import defaultdict


def solution(genres, plays):
    N = len(genres)
    dict1 = defaultdict(int)
    dict2 = defaultdict(list)
    dict3 = defaultdict(list)
    results = []

    for i in range(N):
        genre, play = genres[i], plays[i]
        dict1[genre] += play
        dict2[genre].append(i)
        dict3[genre].append(play)

    for _ in range(len(dict1)):
        max_value = -1
        max_key = None
        for key, item in dict1.items():
            if item > max_value:
                max_value = item
                max_key = key
        # dict1 = {'classic' : 1450, 'pop':3100}
        arr = dict3[max_key]
        if len(arr) == 1:
            results.append(dict2[max_key][0])
            dict1[max_key] = -1
            continue
        for __ in range(2):
            # 이제 arr에서 max인 index를 찾는다.
            max_idx = 0
            for i in range(len(arr)):
                if arr[i] > arr[max_idx]:
                    max_idx = i
            results.append(dict2[max_key][max_idx])
            arr[max_idx] = -1

        dict1[max_key] = -1
    return results


print(solution)