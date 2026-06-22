class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # To make it in O(n)
        n = len(nums)
        summ_all = n * (n+1) // 2

        return summ_all - sum(nums)