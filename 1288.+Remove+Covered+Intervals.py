
# coding: utf-8

# In[ ]:

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = len(intervals)
        intervals.sort(reverse = True, key = lambda x:(x[1],-x[0]))
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0]>=start and intervals[i][1] <= end:
                ans -= 1
            else:
                start = intervals[i][0]
                end = intervals[i][1]
        return ans

