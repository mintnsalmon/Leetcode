
# coding: utf-8

# In[ ]:

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        #p1,p2 = 0
        max_sum = nums[0]
        num_sum = nums[0]
        i=0
        for i in range(0,len(nums)-1):
            if nums[i] < nums[i+1]:
                num_sum+=nums[i+1]
            else:
                num_sum = nums[i+1]
            max_sum = max(max_sum, num_sum)
        return max(max_sum, num_sum)
    

