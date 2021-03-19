
# coding: utf-8

# In[ ]:

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[1])
        arrows = 1
        end_point = points[0][1]
        for ballon_start, ballon_end in points:
            if ballon_start > end_point:
                arrows += 1
                end_point = ballon_end
        return arrows

