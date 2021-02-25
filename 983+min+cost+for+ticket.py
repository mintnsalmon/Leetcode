
# coding: utf-8

# In[ ]:

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        _1day_pass, _7day_pass, _30day_pass = 0, 1, 2
        NOT_Traveling_Day = -1
        dp_cost = [NOT_Traveling_Day for _ in range(366)]
        dp_cost[0] = 0
        
        for day in days:
            dp_cost[day] = 0
            
        for day_i in range(1, 366):   
            if dp_cost[day_i] == NOT_Traveling_Day:
                dp_cost[day_i] = dp_cost[day_i - 1]
            else:
                dp_cost[day_i] = min(dp_cost[ day_i - 1 ]  + costs[ _1day_pass ], dp_cost[ max(day_i - 7, 0) ]  + costs[ _7day_pass ], dp_cost[ max(day_i - 30, 0) ] + costs[ _30day_pass ])

        return dp_cost[365]

