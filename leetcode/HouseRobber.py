class Solution:
    
    def go(self, i, nums, memo):
        if i == len(nums)-1 or i == len(nums) - 2:
            memo[i] = nums[i]
            return memo[i] 
        
        if memo[i] != -1:
            return memo[i]
        
        if i+3 < len(nums):
            memo[i] = max(self.go(i+2, nums, memo), self.go(i+3, nums, memo)) + nums[i]
        else:
            memo[i] = self.go(i+2, nums, memo) + nums[i]
        return memo[i]    
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        n = len(nums)
        memo = [-1 for _ in range(n)]
        self.go(0, nums, memo)
        self.go(1, nums, memo)
        
        return max(memo[0], memo[1])
