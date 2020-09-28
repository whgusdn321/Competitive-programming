midnight = 60*24


def parse(score):
    result = []
    i = 0
    while i < len(score):
        token = ''
        token += score[i]
        if i+1 < len(score) and score[i+1] == '#':
            token += score[i+1]
            i += 2
        else:
            i += 1
        result.append(token)
    return result



def solution(m, musicinfos):
    """

    :param m: 'ABCDEFG'
    :param musicinfos: ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    :return: "HELLO"
    """
    m = parse(m)
    played_songs = []
    for music in musicinfos:
        arr = music.split(',')
        sh = int(arr[0][:2])
        sm = int(arr[0][3:5])
        eh = int(arr[1][:2])
        em = int(arr[1][3:5])
        start = 60 * sh + sm
        end = 60 * eh + em
        if end < start:
            end = midnight

        score = arr[3]
        parsed = parse(score)
        N = len(parsed)
        played = []
        i = 0
        for _ in range(start, end):
            played.append(parsed[i])
            i = (i+1) % N
        played_songs.append((played, end-start, arr[2]))

    candidates = []
    for p in played_songs:
        n = len(p[0])
        mn = len(m)
        for i in range(0, n-mn+1):
            if m == p[0][i:i+mn]:
                candidates.append(p)
                break

    if len(candidates) == 0:
        return '(None)'
    else:
        max_i = 0
        for i in range(len(candidates)):
            if candidates[i][1] > candidates[max_i][1]:
                max_i = i
        return candidates[max_i][2]



print(solution('CC#BCC#BCC#BCC#B' , ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))