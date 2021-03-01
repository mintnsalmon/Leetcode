
# coding: utf-8

# In[ ]:

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def dfs(cur, i, d = {}):
            if i < len(nums) and (i, cur) not in d: 
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))
        
        
        return dfs(0, 0)   
        

