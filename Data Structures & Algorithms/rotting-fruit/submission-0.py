class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source BFS
        # queue up the rotten oranges

        if not grid:
            return 0

        queue = deque()
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append([row, col, 0])
                if grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        # we have the queue loaded up with the rotten oranges and the fresh_count

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_minute = 0

        while queue:
            r, c, minute = queue.popleft() # pop the rotten orange
            max_minute = max(max_minute, minute)
            # travel to nearby - check the count and do a plus 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c 

                #check sanity of the new coord
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append([nr, nc, 1 + minute])

        return max_minute if fresh_count == 0 else -1