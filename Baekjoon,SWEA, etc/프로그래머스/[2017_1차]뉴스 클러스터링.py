import itertools
from collections import defaultdict

# def solution(str1, str2):
#     a = []
#     b = []
#     for i in range(len(str1)-1):
#         aa = str1[i].upper()
#         bb = str1[i+1].upper()
#         if 65<=ord(aa)<=90 and 65<=ord(bb)<=90:
#             a.append(aa+bb)
#     for i in range(len(str2)-1):
#         aa = str2[i].upper()
#         bb = str2[i+1].upper()
#         if 65<=ord(aa)<=90 and 65<=ord(bb)<=90:
#             b.append(aa+bb)
#
#
#     a_visited = [False] * len(a)
#     b_visited = [False] * len(b)
#     #print('a : ', a)
#     #print('b : ', b)
#     #print('a_visited: ',a_visited)
#     #print('b_visited : ',b_visited)
#     kyo = []
#     hap = []
#
#     for i in range(len(a)):
#         if not a_visited[i]:
#             l, m = 1, 0
#             a_visited[i] = True
#             for j in range(i + 1, len(a)):
#                 if not a_visited[j]:
#                     if a[i] == a[j]:
#                         l += 1
#                         a_visited[j] = True
#             for j in range(len(b)):
#                 if not b_visited[j]:
#                     if a[i] == b[j]:
#                         m += 1
#                         b_visited[j] = True
#             kyo.append(min(l, m))
#             hap.append(max(l, m))
#
#     for i in range(len(b)):
#         if not b_visited[i]:
#             m = 1
#             b_visited[i] = True
#             for j in range(i + 1, len(b)):
#                 #print('b_visited : ', b_visited)
#                 if not b_visited[j]:
#                     if b[i] == b[j]:
#                         m += 1
#                         b_visited[j] = True
#             hap.append(m)
#     #print('kyo : ', kyo)
#     #print('hap : ',hap)
#     if not sum(hap) == 0:
#         answer = int(sum(kyo) / sum(hap))
#     else:
#         answer = 1
#
#     return answer * 65536


def solution(str1, str2):
    set1 = []
    set2 = []
    for i in range(len(str1)-1):
        temp = str1[i:i+2].upper()
        if 65<=ord(temp[0])<=90 and 65<=ord(temp[1])<=90:
            set1.append(temp)
    for i in range(len(str2)-1):
        temp = str2[i:i+2].upper()
        if 65<=ord(temp[0])<=90 and 65<=ord(temp[1])<=90:
            set2.append(temp)
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    for char in set1:
        dict1[char] += 1
    for char in set2:
        dict2[char] += 1
    kyo = defaultdict(int)
    hap = defaultdict(int)
    for item in dict1:
        kyo[item] = min(dict1[item], dict2[item])
        hap[item] = max(dict1[item], dict2[item])
    for item in dict2:
        hap[item] = max(dict1[item], dict2[item])
    ans = (sum(kyo.values()) / sum(hap.values())) * 65536
    ans = int(ans)
    return ans
print(solution('handshake', 'shake hands'))