
# coding: utf-8

# In[ ]:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) == 0:
            return ans
        strs.sort()
        j=1
        for i in range(0,len(strs[0])):
            count = 0
            for j in range(len(strs)):
                if strs[0][i]!=strs[j][i]:
                    count += 1
                    break
            if count == 0:
                ans = ans+strs[0][i]
            else:
                break
                
        return ans

