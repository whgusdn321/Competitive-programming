def solution(msg):
    answer = []
    wdict = {ch : i+1 for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    last = 27
    i = 0

    while i < len(msg):
        str = msg[i]
        j = i+1
        while j < len(msg) and str+msg[j] in wdict:
            str += msg[j]
            j += 1
        answer.append(wdict[str])
        if j < len(msg):
            wdict[str+msg[j]] = last
            last += 1
        i = j

    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))