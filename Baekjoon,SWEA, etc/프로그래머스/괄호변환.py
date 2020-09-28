def allright(p):
    stakk = []
    for i in range(len(p)):
        if p[i] == '(':
            stakk.append('(')
        else:
            if stakk and stakk[-1] == '(':
                stakk.pop()
            else:
                return False

    return len(stakk) == 0


def divide(p):
    u = ""
    v = ""
    cnt_l = 0
    cnt_r = 0
    for i in range(len(p)):
        u += p[i]
        if p[i] == '(':
            cnt_l += 1
        else:
            cnt_r += 1
        if cnt_l == cnt_r:
            for j in range(i+1, len(p)):
                v += p[j]
            break
    return u, v


def solution(p):
    if len(p) == 0:
        return ""
    u, v = divide(p)  # v can be empty, but u is not
    if allright(u):
        return u + solution(v)
    else:
        new1 = '(' + solution(v) + ')'
        new2 = ""
        for ch in u[1:-1]:
            if ch == '(':
                new2 += ')'
            else:
                new2 += '('
        return new1 + new2

print(solution("()))((()"))