H, W = None, None


def isCandidate(keys, relation):
    """

    :param keys: [0, 1] or [0,1,2]
    :param relation: HxW array
    :return: True vs False
    """
    global H, W
    boool = True
    items = []
    for i in range(H):
        item = [relation[i][k] for k in keys]
        items.append(item)
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                boool = False
                return boool
    return boool


def solution(relation):
    """

    :param relation:[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    :return:
    """
    global H, W
    H, W = len(relation), len(relation[0])
    candidates = []
    a = [[i] for i in range(W)] #a is keys
    while a:
        for i, key in enumerate(a):
            rmv = []
            if isCandidate(key, relation):
                candidates.append(key.copy())
                rmv.append(i)
        #제거해야할 원소들 제거(가지치기).
        new_a = []
        for i in range(len(a)):
            if i not in rmv:
                new_a.append(a[i])
        a = new_a
        #다음 키들을 추가한다.
        new_a = []
        for i in range(len(a)):
            key = a[i]
            for j in range(0, W):
                if j not in key:
                    new_key = key.copy() + [j]
                    boool = False
                    for candidate in candidates:
                        temp_bool = True
                        for c in candidate:
                            if c in new_key:
                                temp_bool &= True
                            else:
                                temp_bool &= False
                        if temp_bool:
                            boool = True
                            break
                    if not boool:
                        boool2 = True
                        for ki in new_a:
                            if set(ki) == set(new_key):
                                boool2 = False
                        if boool2:
                            new_a.append(new_key)
        a = new_a
    return candidates

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))