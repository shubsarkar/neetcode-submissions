class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return []
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        
        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range (2, len(nums)):
            rob_it = nums[i] + dp[i-2]
            skip_it = dp[i-1]

            dp[i] = max(rob_it, skip_it)

        return dp[-1]
