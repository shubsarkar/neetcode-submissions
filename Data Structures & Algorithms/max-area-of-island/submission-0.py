class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                # we hit the boundary or landed on water
                return 0
            
            area = 1
            grid[r][c] = 0 #mark as visited but also count the area
            
            for nr, nc in directions:
                area += dfs(r + nr, c + nc)
            
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea