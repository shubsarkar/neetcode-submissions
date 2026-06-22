class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}

        for idx, val in enumerate(nums):
            compliment = target - nums[idx]

            if compliment in target_map:
                return [target_map[compliment], idx]
            else:
                target_map[val] = idx

        return []