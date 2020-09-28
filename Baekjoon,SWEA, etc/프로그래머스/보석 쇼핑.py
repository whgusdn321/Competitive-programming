from collections import defaultdict


def solution(gems):
    ans = []
    dict = defaultdict(bool)
    rgems = []
    for gem in gems:
        if not dict[gem]:
            dict[gem] = True
            rgems.append(gem)
    all = len(rgems)

    dict1 = {}
    end = len(gems)-1
    cnt = 0

    for i in range(len(gems)-1, -1, -1):
        if cnt < all:
            dict1[gems[i]] = i
            cnt = len(dict1)
            if cnt == all:
                max_ = i
                for key, val in dict1.items():
                    if val > max_:
                        max_ = val
                end = max_
                ans.append((i+1, end+1))
        else:
            if dict1[gems[end]] == dict1[gems[i]]:  # find new end # find new end # find new end
                dict1[gems[i]] = i
                max_ = i
                for key, val in dict1.items():
                    if val > max_:
                        max_ = val
                end = max_
                ans.append((i+1, end+1))
            else:
                ans.append((i+1, end+1))
                dict1[gems[i]] = i

    dict2 = {}
    end = 0
    cnt = 0
    for i in range(0, len(gems)):
        if cnt < all:
            dict2[gems[i]] = i
            cnt = len(dict2)
            if cnt == all:
                min_ = i
                for key, val in dict2.items():
                    if val < min_:
                        min_ = val
                end = min_
                ans.append((end+1, i+1))
        else:
            if dict2[gems[end]] == dict2[gems[i]]:
                dict2[gems[i]] = i
                min_ = i
                for key, val in dict2.items():
                    if val < min_:
                        min_ = val
                end = min_
                ans.append((end + 1, i + 1))
            else:
                dict2[gems[i]] = i
                ans.append((end+1, i+1))
    ans.sort(key=lambda x:(x[1] - x[0], x[0]))
    print(ans)
    return [ans[0][0], ans[0][1]]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
