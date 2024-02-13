class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            visited.add((i, j))
           
            self.fish += grid[i][j]
            for r,c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_r = r + i
                new_c = c + j
                if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited and grid[new_r][new_c] != 0:
                    dfs(new_r, new_c)
                
            
        
        m = len(grid)
        n = len(grid[0])
        ans = 0
        self.fish = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i,j) not in visited:
                    self.fish = 0
                    dfs(i,j)
                    ans = max(self.fish, ans)
        return ans
        
        