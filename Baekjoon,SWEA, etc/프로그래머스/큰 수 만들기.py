import heapq


# def solution(number, k):
#     N = len(number)
#     arr = []
#
#     for i in range(k):
#         heapq.heappush(arr, -int(number[i]))
#     ans = ''
#     for i in range(k, N):
#         heapq.heappush(arr, -int(number[i]))
#         n = heapq.heappop(arr)
#         n = str(-n)
#         ans += n
#     return ans

def solution(number, k):
    number = [char for char in number]
    cnt = 0
    while cnt < k:
        for i in range(len(number)-1):
            if int(number[i]) < int(number[i+1]):
                #print('i : ', i)
                number.pop(i)
                cnt += 1
                break

    ans = ''.join(number)
    return ans





print(solution('1924', 2))