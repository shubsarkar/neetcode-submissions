class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # to would be mapped to a 1-D so a simple binary search for the target should work
        left, right = 0, rows * cols - 1

        while (left <= right):
            mid = left + (right - left) // 2
            mid_val = matrix[mid // cols][mid % cols] 

            if mid_val == target:
                return True

            if mid_val > target:
                right = mid - 1
            if mid_val < target:
                left = mid + 1

        return False