def parse(file):
    head = ""
    number = ""
    tail = ""
    n = len(file)
    j = 0
    for i in range(n):
        if not ('0' <= file[i] <= '9'):
            head += file[i]
        else:
            j = i
            break
    cnt = 0
    for i in range(j, n):
        if '0' <= file[i] <= '9' and cnt < 5:
            number += file[i]
            cnt += 1
        else:
            j = i
            break
    for i in range(j, n):
        tail += file[i]

    return (head, number, tail)


def solution(files):
    ans = []
    for file in files:
        head, number, tail = parse(file)
        ans.append((head.lower(), int(number), tail, file))
    ans.sort(key=lambda x:(x[0], x[1]))
    ans = [a[3] for a in ans]
    return ans
print(solution(	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))