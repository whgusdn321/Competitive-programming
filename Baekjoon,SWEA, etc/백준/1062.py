n, k = map(int, input().split())
strings = []
alphbet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0,\
           'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,\
           'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0,\
           'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

for _ in range(n):
    temp = input()
    strings.append(temp)

for string in strings:
    stack = []
    for char in string:
        if char not in stack:
            alphbet[char] += 1
            stack.append(char)

print('alphbet : ',alphbet)
allowedchrs = []

for _ in range(k):
    max_item = -1
    max_key = None
    for key, item in alphbet.items():
        if item > max_item:
            max_key = key
            max_item = item
    allowedchrs.append(max_key)
    alphbet[max_key] = -1

print('allowedchrs : ', allowedchrs)

cnt = 0
for string in strings:
    boool = True
    for char in string:
        if char in allowedchrs:
            continue
        else:
            boool = False
            break
    if boool:
        cnt += 1
print(cnt)