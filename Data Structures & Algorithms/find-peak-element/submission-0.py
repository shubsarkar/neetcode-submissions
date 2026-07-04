class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # it has to be visualized as a 2D peak
        left, right = 0, len(nums) - 1

        while (left < right):
            mid = left + (right - left) // 2

            if (nums[mid] < nums[mid+1]):
                # there is a forming peak on the right side
                left = mid + 1
            else:
                # this could be a probable peak so we keep this idx included and search in the left half
                right = mid

        return left
