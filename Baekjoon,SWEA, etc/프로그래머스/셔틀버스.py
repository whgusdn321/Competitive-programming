from collections import defaultdict


def convert(num):
    h = num // 60
    m = num % 60
    ret = ""
    if h<10:
        ret += '0'
        ret += str(h)
    else:
        ret += str(h)
    ret += ":"
    if m < 10:
        ret += '0'
        ret += str(m)
    else:
        ret += str(m)
    return ret


def solution(n, t, m, timetable):
    times = []
    bus_times = [540]
    for time in timetable:
        hh = int(time[:2])
        mm = int(time[3:])
        times.append(60*hh + mm)
    times.sort()
    start = 540
    n -= 1
    while n > 0:
        start += t
        bus_times.append(start)
        n -= 1
    print(bus_times)
    print(times)
    dict = defaultdict(list)
    i = 0
    for bus_time in bus_times:
        cnt = 0
        for j in range(i, len(times)):
            if cnt == m or times[j] > bus_time:
                i = j
                break
            cnt += 1
            dict[bus_time].append(times[j])
    print(dict)
    if len(dict[bus_times[-1]])<m:
        return convert(bus_times[-1])
    else:
        return convert(dict[bus_times[-1]][-1]-1)


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))