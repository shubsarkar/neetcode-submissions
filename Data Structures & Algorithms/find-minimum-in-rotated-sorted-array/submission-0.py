class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we apply the right hand rule in this case, as it's sorted by rotated ....__..

        left, right = 0, len(nums) - 1

        while (left < right):
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]: 
                # I am standing at a hill and the right is smaller, the drop must be in between (confident)
                left = mid + 1
            else:
                # I am standing at a lower value but this could be a solution as well, so need to retain it
                right = mid

        return nums[left]