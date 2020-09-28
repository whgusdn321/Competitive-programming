from collections import defaultdict


def pos1(x, y, dict1, dict2):
    if y == 0:
        return True
    if dict1[(x, y-1)]:
        return True
    if dict2[(x, y)] or dict2[(x-1, y)]:
        return True
    return False


def pos2(x, y, dict1, dict2):
    if dict1[(x, y-1)] or dict1[(x+1, y-1)]:
        return True
    if dict2[(x-1, y)] and dict2[(x+1, y)]:
        return True
    return False


def solution(n, build_frame):
    answer = []
    dict1 = defaultdict(bool)
    dict2 = defaultdict(bool)
    for x, y, a, b in build_frame:
        if b:
            if a == 0:
                if pos1(x, y, dict1, dict2):
                    dict1[(x, y)] = True
            else:
                if pos2(x, y, dict1, dict2):
                    dict2[(x, y)] = True
        else:  # delete
            pos = True
            if a == 0:
                dict1[(x, y)] = False
                if dict1[(x, y+1)]:
                    pos &= pos1(x, y+1, dict1, dict2)
                if dict2[(x, y+1)]:
                    pos &= pos2(x, y+1, dict1, dict2)
                if dict2[(x-1, y+1)]:
                    pos &= pos2(x-1, y+1, dict1, dict2)
                if not pos:
                    dict1[(x, y)] = True
            else:  # a == 1
                dict2[(x, y)] = False
                if dict1[(x, y)]:
                    pos &= pos1(x, y, dict1, dict2)
                if dict1[(x+1, y)]:
                    pos &= pos1(x+1, y, dict1, dict2)
                if dict2[(x-1, y)]:
                    pos &= pos2(x-1, y, dict1, dict2)
                if dict2[(x+1, y)]:
                    pos &= pos2(x+1, y, dict1, dict2)
                if not pos:
                    dict2[(x, y)] = True
    for x, y in dict2:
        if dict2[(x, y)]:
            answer.append([x, y, 1])
    for x, y in dict1:
        if dict1[(x, y)]:
            answer.append([x, y, 0])
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return answer


print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))