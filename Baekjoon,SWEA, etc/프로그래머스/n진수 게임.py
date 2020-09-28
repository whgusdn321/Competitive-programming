dict1 = {10:"A", 11:"B", 12:"C", 13 : "D", 14:"E", 15 : "F"}


def convert(num, p):
    if num == 0:
        return '0'
    ret = ""
    while num:
        if num%p < 10:
            ret += str(num%p)
        else:
            ret += dict1[num%p]
        num //= p
    return ret[::-1]


def solution(n, t, m, p):
    print(convert(0, 2))
    num = 0
    ret = []
    for _ in range(t*m):
        s = convert(num, n)
        for ch in s:
            ret.append(ch)
        num += 1
    print(ret)
    p -= 1
    ans = ""
    while len(ans) < t:
        ans += ret[p]
        p += m
    return ans

print(solution(16, 16, 2, 1))