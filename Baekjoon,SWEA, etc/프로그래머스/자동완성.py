from copy import deepcopy
dicttt = { a: b for (a, b) in zip('abcdefghijklmnopqrstuvwxyz', [0]*len('abcdefghijklmnopqrstuvwxyz'))}


def solution(words):
    N = len(words)
    results = [''] * N
    max_n = 0
    for word in words:
        if len(word) > max_n:
            max_n = len(word)

    for i in range(0, max_n):
        print('words : ', words)
        dictt = deepcopy(dicttt)

        for word in words:
            if i < len(word):
                dictt[word[i]] += 1
        print('dictt : ', dictt)
        for j in range(N):
            if i < len(words[j]):
                if dictt[words[j][i]] > 1:
                    results[j] += words[j][i]
                else:
                    results[j] += words[j][i]
                    words[j] = ''

    summ = 0
    for char in results:
        summ += len(char)




    return summ



print(solution(['go','gone','guild']))