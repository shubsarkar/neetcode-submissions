class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we make two stacks - to track the shortest on left and right for each index
        # two separate arrays for left and right - indices for the left and right limit
        n = len(heights)
        left_limit = [-1] * n # -1 to allow the rectangle being formed to -1
        right_limit = [n] * n # to allow the rectangle to include the final idx n-1, the boundary pushed to n

        # so that right - left - 1 makes sense

        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_limit[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_limit[i] = stack[-1]
            stack.append(i)

        maxArea = 0

        for i in range(n):
            width = right_limit[i] - left_limit[i] - 1
            maxArea = max(maxArea, width * heights[i])

        return maxArea