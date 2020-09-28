Nor_m = {1 : 31, 2: 28, 3:31 , 4:30 , 5:31 , 6:30 , 7:31 , 8:31 , 9:30 , 10:31 , 11:30 , 12:31}
Yoon_m = {1 : 31, 2: 29, 3:31 , 4:30 , 5:31 , 6:30 , 7:31 , 8:31 , 9:30 , 10:31 , 11:30 , 12:31}
yoonsecs = (31+29+31+30+31+30+31+31+30+31+30+31)*(3600*24)
norsecs = (31+28+31+30+31+30+31+31+30+31+30+31)*(3600*24)


def isYoon(year):
    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False


def tosec(string):
    '''2017/07/16 03:05:00'''
    if len(string) == 20:
        year = int(string[0:5])
        month = int(string[6:8])
        day = int(string[9:11])
        hour = int(string[12:14])
        minute = int(string[15:17])
        sec = int(string[18:20])

    else:
        year = int(string[0:4])
        month = int(string[5:7])
        day = int(string[8:10])
        hour = int(string[11:13])
        minute = int(string[14:16])
        sec = int(string[17:19])
        #print(year, month, day, hour, minute, sec)
    if isYoon(year):
        monthdays = 0
        for i in range(1, month):
            monthdays += Yoon_m[i]
        monthdays += day
    else:
        monthdays = 0
        for i in range(1, month):
            monthdays += Nor_m[i]
        monthdays += day

    total = sec + minute * 60 + hour * 3600 + (monthdays-1) *(3600*24)
    return total, year


def find_month_day(year, left):
    #print('left : ', left)
    if isYoon(year):
        i = 1
        while left - (3600*24)*Yoon_m[i] > 0:
            left -= (3600*24)*Yoon_m[i]
            i += 1
        month = i

        i = 1
        while left - (3600*24) > 0:
            left -= (3600*24)
            i += 1
        days = i

        cnt = 0
        while left - 3600 >0:
            left -= 3600
            cnt +=1

        hour = cnt


        cnt = 0
        while left - 60 > 0:
            left -= 60
            cnt += 1
        minute = cnt

        sec = left
    else:
        i = 1
        while left - (3600 * 24) * Nor_m[i] > 0:
            left -= (3600 * 24) * Nor_m[i]
            i += 1
        month = i

        i = 1
        while left - (3600 * 24) > 0:
            left -= (3600 * 24)
            i += 1
        days = i

        cnt = 0
        while left - 3600 > 0:
            left -= 3600
            cnt += 1

        hour = cnt

        cnt = 0
        while left - 60 > 0:
            left -= 60
            cnt += 1
        minute = cnt

        sec = left
    #print('inside func : ',month, days, hour, minute, sec)
    return month, days, hour, minute, sec




testcases = int(input())

for testcase in range(1, testcases+1):
    string = input()
    togo = int(input(), 2)
    #print('togo : ', togo)

    now, cyear = tosec(string)
    if isYoon(cyear):
        left = yoonsecs - now
    else:
        left = norsecs - now

    if togo < left:
        month, day, hour, minute, sec = find_month_day(cyear, now+togo) # 종료조건
        print("#{} {:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(testcase, cyear, month, day, hour, minute, sec))
        continue
    else:
        togo -= left
        cyear += 1

    while 1:
        if isYoon(cyear):
            if togo < yoonsecs:
                month, day, hour, minute, sec = find_month_day(cyear, togo) #종료조건
                print("#{} {:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(testcase, cyear, month, day, hour, minute,
                                                                             sec))
                break
            else:
                togo -= yoonsecs
                cyear += 1
        else:
            if togo < norsecs:
                month, day, hour, minute, sec = find_month_day(cyear, togo) #종료조건
                print("#{} {:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(testcase, cyear, month, day, hour, minute,
                                                                             sec))
                break
            else:
                togo -= norsecs
                cyear += 1


