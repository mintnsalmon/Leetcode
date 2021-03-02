
# coding: utf-8

# In[ ]:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        ans = [0] * n        
        left[0] = 1
        right[n - 1] = 1
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        for i in range(1, n):
            right[n-i-1] = nums[n-i] * right[n-i]
        for i in range(n):
            ans[i] = left[i] * right[i]
        return ans

