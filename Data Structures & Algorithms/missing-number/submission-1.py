class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss = 0

        all_num = set(nums)

        for i in range(0, len(nums) + 1):
            if i not in all_num:
                miss = i

        return miss