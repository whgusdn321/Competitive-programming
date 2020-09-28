import itertools

# permutations = []
#
#
# def make_permutations(nn, n, permutation, visited):
#     '''
#     if n == 4, create [[0,1,2,3],[0,1,3,2],[0,2,3,4] . . .]
#     '''
#     if len(permutation) == nn:
#         permutations.append(permutation)
#         return
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             permutation.append(i)
#             make_permutations(nn, n, permutation.copy(), visited.copy())
#             permutation.pop()
#             visited[i] = False
#
# def isprime(str_num):
#     num = int(str_num)
#     if num == 1:
#         return False
#     flag = True
#     for i in range(2, num//2+1):
#         if num %i == 0:
#             flag = False
#             break
#     return flag
#
#
# def solution(numbers):
#     global permutations
#     n = len(numbers)
#     for nn in range(1, n+1):
#         visited = [False] * n
#         make_permutations(nn, n, [], visited)
#
#     cnt = 0
#
#     numberVisited = []
#
#     for permutation in permutations:
#         number =''
#         for index in permutation:
#             number += numbers[index]
#
#         j = -1
#         while j != len(number)-1 and number[j+1] == '0':
#             j += 1
#
#         if j == len(number)-1:
#             continue
#         else:
#             number = number[j+1:]
#             if number not in numberVisited:
#                 numberVisited.append(number)
#                 if isprime(number):
#                     cnt += 1
#     return cnt


def isPrime(num):
    if num <= 1 :
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


def solutions(numbers):
    sett = set([])
    N = len(numbers)
    cnt = 0
    for n in range(1, N+1):
        for permu in itertools.permutations(numbers, n):
            #print('permu : ', ''.join(permu))
            candidate = int(''.join(permu))
            sett.add(candidate)
    for number in sett:
        if isPrime(number):
            cnt += 1
    return cnt
print(solutions('011'))