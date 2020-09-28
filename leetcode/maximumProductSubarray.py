class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo1 = [[0, 0] for _ in range(len(nums))]
        memo2 = [[0, 0] for _ in range(len(nums))]
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] < 0:
            return nums[0]
        
        if nums[-1] < 0:
            memo1[-1][0] = nums[-1]
            memo1[-1][1] = 0
        else:
            memo1[-1][0] = 0
            memo1[-1][1] = nums[-1]
        
        if nums[0] < 0:
            memo2[0][0] = nums[0]
            memo2[0][1] = 0
        else:
            memo2[0][0] = 0
            memo2[0][1] = nums[0]
        
        for i in range(len(nums) -2 , -1, -1):
            if nums[i] < 0:
                if memo1[i+1][1] == 0:
                    memo1[i][0] = nums[i]
                else:
                    memo1[i][0] = memo1[i+1][1] * nums[i]
                memo1[i][1] = memo1[i+1][0] * nums[i]
            elif nums[i] > 0:
                if memo1[i+1][1] == 0:
                    memo1[i][1] = nums[i]
                else:
                    memo1[i][1] = memo1[i+1][1] * nums[i]
                memo1[i][0] = memo1[i+1][0] * nums[i] 
            else:
                memo1[i][0] = 0
                memo1[i][1] = 0
                
        for i in range(1, len(nums)):
            if nums[i] < 0:
                if memo2[i-1][1] == 0:
                    memo2[i][0] = nums[i]
                else:
                    memo2[i][0] = memo2[i-1][1] * nums[i]
                memo2[i][1] = memo2[i-1][0] * nums[i]
            elif nums[i] > 0:
                if memo2[i-1][1] == 0:
                    memo2[i][1] = nums[i]
                else:
                    memo2[i][1] = memo2[i-1][1] * nums[i]
                memo2[i][0] = memo2[i-1][0] * nums[i] 
            else:
                memo2[i][0] = 0
                memo2[i][1] = 0
        
        ans = -999999
        for a, b in memo1:
            ans = max(ans, a)
            ans = max(ans, b)
        for a, b in memo2:
            ans = max(ans, a)
            ans = max(ans, b)
        print(memo1)
        print(memo2)
        return ans
