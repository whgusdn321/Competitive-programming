candidates = []
nums= None


def dfs(k, num):
    global nums, candidates
    if k == len(nums):
        candidates.append(num)
        return
    num1 = num - nums[k]
    num2 = num + nums[k]
    dfs(k+1, num1)
    dfs(k+1, num2)


def solution(numbers, target):
    global nums
    nums = numbers
    dfs(0, 0)

    #print('candidates:', candidates)
    cntt = 0
    for i in candidates:
        if i == target:
            cntt += 1
    return cntt

solution([1,1,1,1,1], 3)