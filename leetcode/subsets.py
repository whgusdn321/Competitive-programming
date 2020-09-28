class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        k = 0
        rets = []
        for i in range(1<<n, 1<<n+1):
            bitmask = bin(i)[3:]
            ret = [nums[i] for i, bit in enumerate(bitmask) if bit == '0']
            rets.append(ret)
        # while k < 2**n:
        #     ret = []
        #     for i in range(n):
        #         if 1<<i & k:
        #             ret.append(nums[i])
        #     k+=1
        #     rets.append(ret)
        return rets
