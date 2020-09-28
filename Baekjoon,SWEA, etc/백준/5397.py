import sys
from collections import deque

read = lambda :sys.stdin.readline().rstrip()

test_cases = int(read())
for _ in range(test_cases):
    arr = input()
    stack1 = []
    stack2 = []
    for char in arr:
        if char == '<':
            if stack1:
                temp = stack1.pop()
                stack2.append(temp)
        elif char == '>':
            if stack2:
                temp = stack2.pop()
                stack1.append(temp)
        elif char == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(char)
    while stack2:
        temp = stack2.pop()
        stack1.append(temp)
    for char in stack1:
        print(char, end='')
    print()


















#     queue = deque([a for a in read()])
#     i = 0
#     j = 1
#     cur = 0
#     arr = []
#     while queue:
#         oper = queue.popleft()
#         if oper == '<':
#             if cur-1 > -1:
#                 cur -= 1
#         elif oper == '>':
#             if cur+1 < j:
#                 cur += 1
#         elif oper == '-':
#             if cur-1 > -1:
#                 cur -= 1
#                 arr.pop(cur)
#                 j -= 1
#         else:
#             arr.insert(cur, oper)
#             cur += 1
#             j += 1
#     for item in arr:
#         print(item, end='')
