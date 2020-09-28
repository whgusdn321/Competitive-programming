import sys
read = lambda :sys.stdin.readline().rstrip()

N, L = map(int, read().split())
maap = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)

cnt = 0


def inspect2(arr, L):
    visited = [False] * len(arr)
    i = 0
    while i < len(arr) - 1:
    #for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            i += 1
            continue
        elif arr[i] == arr[i+1] + 1:
            if i + L < len(arr):
                temp = arr[i+1]
                boool = True
                for j in range(i+1, i+L+1):
                    if arr[j] != temp or visited[j]:
                        boool = False
                        break
                if boool == False:
                    return False
                else:
                    for j in range(i+1, i+L+1):
                        visited[j] = True
                    i += L
                    continue
            else:
                return False
        elif arr[i] == arr[i+1] -1:
            if i - L +1 >= 0:
                temp = arr[i]
                boool = True
                for j in range(i, i-L, -1):
                    if arr[j] != temp or visited[j]:
                        boool = False
                        break
                if boool == False:
                    return False
                else:
                    for j in range(i, i-L, -1):
                        visited[j] = True
                    i += 1
                    continue
            else:
                return False
        else:
            return False

    return True





# def inspect(arr, L):
#     i = 0
#     while i < len(arr) - 1:
#         if arr[i] == arr[i+1]:
#             i += 1
#             continue
#         elif arr[i] == arr[i+1] + 1:
#             j = i + 1
#             l = j + L
#             if l > len(arr):
#                 return False
#             else:
#                 for k in range(j, l):
#                     if arr[k] != arr[j]:
#                         return False
#                 i += L
#                 continue
#         elif arr[i] == arr[i+1] - 1:
#             j = i-(L-1)
#             if j < 0:
#                 return False
#             else:
#                 for k in range(j, i):
#                     if arr[k] != arr[i]:
#                         return False
#                 for k in range(i-2L+1, )
#                 i += 1
#                 continue
#         else:
#             return False
#     if i == len(arr) - 1:
#         return True

# arr = [1, 1, 1, 2, 2, 2]
# L = 2
# print(inspect(arr, L))


# for i in range(N):
#     #rows
#     arr = maap[i]
#     boool = inspect(arr, L)
#     if boool:
#         print('bool1 , arr: ',arr)
#         cnt += 1
#         continue
#     else:
#         arr2 = [arr[-i] for i in range(1, len(arr)+1)]
#         boool = inspect(arr2, L)
#         if boool:
#             print('bool2 , arr: ', arr)
#             cnt += 1


# for j in range(N):
#     #coloums
#     arr = []
#     for i in range(N):
#         arr.append(maap[i][j])
#     #now n'th row is arr
#     boool = inspect(arr, L)
#     if boool:
#         print('bool11 arr1 : ',arr)
#         cnt += 1
#         continue
#     else:
#         arr2 = [arr[-i] for i in range(1, len(arr)+1)]
#         boool = inspect(arr2, L)
#         if boool:
#             print('bool22 arr1 : ', arr)
#             cnt += 1

for i in range(N):
    #rows
    arr = maap[i]
    boool = inspect2(arr, L)
    if boool:
        #print('bool1 , arr: ',arr)
        cnt += 1

for j in range(N):
    #coloums
    arr = []
    for i in range(N):
        arr.append(maap[i][j])
    boool = inspect2(arr, L)
    if boool:
        #print('bool2 arr2 : ',arr)
        cnt += 1


print(cnt)