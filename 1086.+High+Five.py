
# coding: utf-8

# In[ ]:

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        result = []
        for each in items:
            if each[0] in mapping:
                mapping[each[0]].append(each[1])
            else:
                mapping[each[0]] = [each[1]]
        for x,y in mapping.items():
            y.sort(reverse = True)
            i = 0
            total = 0
            while i<5 and i<len(y):
                total += y[i]
                i += 1
            result.append([x,total//i])
            result.sort(key = lambda x:x[0])
        return result


