def solution(lines):
    f_s = []
    for line in lines:
        a = line.split()
        #print('a : ', a)
        hh, mm, ss, sss = a[1][0:2], a[1][3:5], a[1][6:8], a[1][8:12]

        T = a[2][:-1]
        finishtime = 3600 * int(hh) + 60 * int(mm) + int(ss) + float(sss)
        starttime = finishtime - (float(T) - 0.001)
        f_s.append((starttime, finishtime))
    #print('f_s : ', f_s)
    cnts = []
    for i in range(len(f_s)):
        a,b = (f_s[i][0], f_s[i][0] + 0.9999)
        cnt = 0
        for j in range(len(f_s)):
            c, d = f_s[j][0], f_s[j][1]
            if c <= a <= d <= b or a <= c <= b <= d or a<=c<=d<=b or c<=a<=b<=d:
                cnt += 1
        cnts.append(cnt)

        a, b = (f_s[i][1], f_s[i][1] + 0.9999)
        cnt = 0
        for j in range(len(f_s)):
            #print('a : {} b : {} c : {} d : {}'.format(a, b, c, d))
            c, d = f_s[j][0], f_s[j][1]
            if c <= a <= d <= b or a <= c <= b <= d or a <= c <= d <= b or c <= a <= b <= d:
                cnt += 1
        cnts.append(cnt)

        a, b = (f_s[i][1]-0.9999, f_s[i][1])
        cnt = 0
        for j in range(len(f_s)):
            c, d = f_s[j][0], f_s[j][1]
            if c <= a <= d <= b or a <= c <= b <= d or a<=c<=d<=b or c<=a<=b<=d:
                cnt += 1
        cnts.append(cnt)

        a, b = (f_s[i][0] - 0.9999, f_s[i][0])
        cnt = 0
        for j in range(len(f_s)):
            c, d = f_s[j][0], f_s[j][1]
            if c <= a <= d <= b or a <= c <= b <= d or a <= c <= d <= b or c <= a <= b <= d:
                cnt += 1
        cnts.append(cnt)


    return max(cnts)

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))