class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if (grid[0][0] == 1 or grid[rows-1][cols-1] == 1):
            return -1 # traversal not possible

        queue = deque()
        grid[0][0] = 1 # mark the first as visited
        queue.append((0,0)) # append the start node to the queue

        distances = [(-1,0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while queue:
            row, col = queue.popleft() # deque the first element

            if row == rows - 1 and col == cols - 1: 
                return grid[row][col]

            for r, c in distances:
                nr, nc = r + row, c + col

                if (nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 0):
                    # this makes the new choice in the range and also the new path is not having any blockage
                    grid[nr][nc] = grid[row][col] + 1 # mark as visited
                    queue.append((nr, nc)) # append in the queue to process it next
                
        return -1

