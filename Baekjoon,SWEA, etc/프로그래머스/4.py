def solution(k, room_number):
    res = []
    # rooms = [0]*k
    next = []
    for i in range(k):
        next.append(i)

    for n in room_number:
        n = n - 1
        if rooms[n] == 0:
            rooms[n] = 1
            res.append(n + 1)
            next[n] = n + 1
        else:
            temp = []
            while next[n] != n:
                temp.append(n)
                n = next[n]
            rooms[n] = 1
            res.append(n + 1)
            next[n] = n + 1
            for nn in temp:
                next[nn] = n + 1

    return res