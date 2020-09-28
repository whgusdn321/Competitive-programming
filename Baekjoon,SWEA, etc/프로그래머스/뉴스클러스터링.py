from collections import defaultdict


def solution(str1, str2):
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    keys = []
    for i in range(len(str1) - 1):
        str = str1[i:i+2]
        str = str.lower()
        if 'a'<=str[0]<='z' and 'a' <=str[1]<='z':
            dict1[str] += 1
            if str not in keys:
                keys.append(str)
    for i in range(len(str2) - 1):
        str = str2[i:i+2]
        str = str.lower()
        if 'a'<=str[0]<='z' and 'a' <=str[1]<='z':
            dict2[str] += 1
            if str not in keys:
                keys.append(str)
    a = 0
    b = 0
    for key in keys:
        a += min(dict1[key], dict2[key])
        b += max(dict1[key], dict2[key])
    if a==0 and b==0:
        return 0
    else:
        return int((a/b)*65536)

print(solution("FRANCE", "french"))