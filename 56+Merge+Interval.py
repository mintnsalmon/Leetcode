
# coding: utf-8

# In[7]:

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()



# In[8]:

result = []
for interval in intervals:
    if not result or result[-1][1] < interval[0]:
        result.append(interval)
    else:
        result[-1][1] = max(result[-1][1], interval[1])
print(result)

    
    
    


# In[ ]:



