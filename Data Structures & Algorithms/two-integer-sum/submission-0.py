class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_n = {}

        for idx, item in enumerate(nums):
            compliment = target - item

            if compliment in dict_n:
                return [dict_n[compliment], idx]

            else:
                dict_n[item] = idx