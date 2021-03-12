
# coding: utf-8

# In[ ]:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        available = 0
        room = 0  
        for each in intervals:
            starts.append(each[0])
            ends.append(each[1])
        starts.sort()
        ends.sort()
        s = e = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    room += 1
                else:
                    available -= 1
                s+=1
            else:
                available += 1
                e += 1
        return room

