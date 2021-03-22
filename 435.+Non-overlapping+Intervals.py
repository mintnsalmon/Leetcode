
# coding: utf-8

# In[ ]:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[1])
        ans = 0
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_end:
                ans += 1
            else:
                cur_start = intervals[i][0]
                cur_end = intervals[i][1]
        return ans

