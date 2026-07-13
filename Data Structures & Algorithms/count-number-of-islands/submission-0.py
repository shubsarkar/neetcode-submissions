class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # can do DFS once we find a 1, from there explore H and V, till we continue finding 1 - 
        # counted as 1 island

        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        island_count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # we have found a start point, start dfs
                    dfs(r, c)
                    island_count += 1

        return island_count



    