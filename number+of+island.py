
# coding: utf-8

# In[ ]:

class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        def dfs(i, j):
            count = 0 
            
            if visited[i][j]: 
                return 0
            else:
                visited[i][j] = 1 
            
            for col in [j-1, j+1]: 
                if col>=0 and col<num_cols:
                    if visited[i][col]==0 and grid[i][col]=="1":
                        count += dfs(i, col)
                        
            
            for row in [i-1, i+1]:
                if row>=0 and row<num_rows: 
                    if visited[row][j]==0 and grid[row][j]=="1":
                        count += dfs(row, j)
                        
            return count + 1  
        
        
        visited = [[0 for j in range(num_cols)] for i in range(num_rows)]
        
        
        islands = 0
        
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j]=="1": 
                    if dfs(i,j)>0: 
                        islands += 1
                    
                    
        

