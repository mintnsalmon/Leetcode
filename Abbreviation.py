
# coding: utf-8

# In[ ]:

class Solution(object):
    def generateAbbreviations(self, word):
        res = []
        self.dfs(word, 0, res)
        return res

    def dfs(self, word, index, r):
        r.append(word)
        for s in range(1, len(word) + 1):
            for i in range(index, len(word)):
                if len(word) - i >= s:
                    self.dfs(word[:i]+str(s)+word[i+s:], i+len(str(s))+1, r)

