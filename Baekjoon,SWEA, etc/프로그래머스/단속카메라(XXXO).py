def compare(elem):
    return abs(elem[1] - elem[0])


def solution(routes):
    #rouutes = routes.copy()
    # for ar in routes:
    #     ar.sort()
    routes.sort(key=compare)
    n = len(routes)
    cnt = 0
    for i in range(len(routes)):
        if routes[i] != -1:
            a , b = routes[i][0], routes[i][1]
            indexs =[i]
            for j in range(i+1, len(routes)):
                if routes[j] != -1:
                    c, d = routes[j][0], routes[j][1]
                    if c<=a<=d<=b:
                        indexs.append(j)
                        #a,b = a,d
                    elif a<=c<=b<=d:
                        indexs.append(j)
                        #a,b = c, b
                    elif a<=c<=d<=b:
                        indexs.append(j)
                        #a,b = c,d
                    elif c<=a<=b<=d:
                        indexs.append(j)
                        #a,b = a, b
            for index in indexs:
                routes[index] = -1
            cnt += 1
    return cnt

#print(solution([[0, 1], [0, 1], [2, 2]]))