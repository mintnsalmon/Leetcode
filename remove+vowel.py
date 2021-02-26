
# coding: utf-8

# In[ ]:

class Solution:
    def removeVowels(self, s: str) -> str:
        ans = ""
        vowels = ['a','e','i','o','u']
        if len(s) == 0:
            return ""

        for each in s:
            if each not in vowels:
                ans += each
        return ans
                

