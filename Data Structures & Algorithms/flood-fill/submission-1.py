class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])

        orig = image[sr][sc]

        # already has the same color
        if orig == color:
            return image

        stack = [(sr, sc)]
        directions = [(-1,0), (1,0), (0, -1), (0,1)]

        while stack:
            r, c = stack.pop()
            image[r][c] = color

            for row, col in directions:
                nr, nc = r + row, c + col
                
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig:
                    stack.append((nr, nc))

        return image

