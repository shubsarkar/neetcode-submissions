class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:

            # find the mid
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return result