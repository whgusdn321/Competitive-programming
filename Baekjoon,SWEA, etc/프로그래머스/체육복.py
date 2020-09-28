def solution(n, lost, reserve):
    cnt = 0
    visited = {}
    weird = []
    for l in lost:
        if l in reserve:
            weird.append(l)
    for item in weird:
        lost.remove(item)
        reserve.remove(item)

    for res in reserve:
        visited[res] = False
    lost.sort()
    for l in lost:
        if l - 1 in reserve and not visited[l - 1]:
            visited[l - 1] = True
            cnt += 1
        elif l + 1 in reserve and not visited[l + 1]:
            visited[l + 1] = True
            cnt += 1
        else:
            None
    return n - (len(lost) - cnt)