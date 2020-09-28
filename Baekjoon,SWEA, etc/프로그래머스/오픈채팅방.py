def solution(record):
    dict1 = {}
    results = []
    for rec in record:
        tmp = rec.split()
        if tmp[0] == "Enter":
            results.append((1, tmp[1]))
            dict1[tmp[1]] = tmp[2]
        elif tmp[0] == "Leave":
            results.append((0, tmp[1]))
        else:  # change
            dict1[tmp[1]] = tmp[2]

    real = []
    for a, id in results:
        if a == 1:
            real.append("{}님이 들어왔습니다.".format(dict1[id]))
        else:
            real.append("{}님이 나갔습니다.".format(dict1[id]))
    return real

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))