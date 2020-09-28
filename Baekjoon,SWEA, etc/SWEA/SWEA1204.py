test_cases = int(input())
for _ in range(test_cases):
    test_case = int(input())
    arr = [int(a) for a in input().split()]
    #print('cnt : ',cnt)
    nums = [0] * 101
    visited = [False]*len(arr)

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            cnt = 1
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    visited[j] = True
                    cnt += 1
            nums[arr[i]] = cnt
    max_idx = 100
    #print('nums : ',nums)
    for i in range(100, -1, -1):
        if nums[i] > nums[max_idx]:
            max_idx = i
    print("#{} {}".format(test_case, max_idx))