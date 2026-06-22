class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            target_idx = abs(nums[i]) - 1

            if nums[target_idx] > 0:
                nums[target_idx] = - nums[target_idx]

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)

        return result