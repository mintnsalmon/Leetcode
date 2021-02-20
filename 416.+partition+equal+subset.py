
# coding: utf-8

# In[ ]:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1: 
            return False
        half_sum = total_sum//2
        dp = [False]*(half_sum+1)
        dp[0] = True
        for num in nums:
            for value in range(half_sum,num-1,-1):
                dp[value] = dp[value] or dp[value-num]
        return dp[-1]

