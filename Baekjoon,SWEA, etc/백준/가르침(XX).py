alphabet = {a:b for a, b in zip('abcdefghijklmnopqrstuvwxyz', [False]*len('abcdefghijklmnopqrstuvwxyz'))}
N, K = map(int, input().split())
words = []
cnt = 0

for _ in range(N):
    word = input()
    words.append(word)

for char in 'antic':
    alphabet[char] = True
    cnt += 1

if cnt > K:
    result = 0
    print(result)
else:
    result = 0
    new_words = []
    for word in words:
        temp = ''
        for char in word:
            if alphabet[char]:
                continue
            else:
                if char not in temp:
                    temp += char
        new_words.append(temp)
    _new_words = []
    for i in range(len(new_words)):
        _cnt = 0
        for j in range(len(new_words)):
            if i != j:
                if new_words
    # print('words : ', words)
    # print('new_words : ',new_words)
    # print('alphabet : ', alphabet)
    new_words.sort(key=lambda x:len(x))
    for word in new_words:
        boool = True
        for char in word:
            if not alphabet[char]:
                if cnt < K:
                    alphabet[char] = True
                    cnt += 1
                else:
                    boool = False
                    break
            else:
                continue
        if boool:
            result += 1



