def solution(expression):
    operator = []
    operand = []
    tmp = ""
    for i in range(len(expression)):
        if '0' <= expression[i] <= '9':
            tmp += expression[i]
        else:
            operand.append(int(tmp))
            operator.append(expression[i])
            tmp = ""
    operand.append(int(tmp))
    # print(operator)
    # print(operand)
    permu = ["*+-", "*-+", "+*-", "+-*", "-+*", "-*+"]
    ans = 0
    for per in permu:
        opt = operator.copy()
        opr = operand.copy()
        pidx = 0
        while len(opr) > 1:
            new_opr = [opr[0]]
            new_opt = []
            for i in range(len(opt)):
                if opt[i] != per[pidx]:
                    new_opr.append(opr[i+1])
                    new_opt.append(opt[i])
                else:
                    last = new_opr[-1]
                    new_opr.pop()
                    if per[pidx] == '*':
                        new_opr.append(last * opr[i+1])
                    elif per[pidx] == '+':
                        new_opr.append(last + opr[i + 1])
                    else:
                        new_opr.append(last - opr[i + 1])
            pidx += 1
            opr = new_opr
            opt = new_opt
        ans = max(ans, abs(opr[0]))

    return ans

print(solution("50*6-3*2"))