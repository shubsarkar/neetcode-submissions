class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            # ask when iterating over the next element if you would want to include in the sum
            if currSum < 0 and nums[i] > 0:
                currSum = 0
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(maxSum, currSum)

        return maxSum

