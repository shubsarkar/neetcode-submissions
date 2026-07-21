class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window = 0
        best_ans = float('inf')

        for right in range(len(nums)):
            # add element to window
            window += nums[right]

            while window >= target: 
                # now the window is valid, we need the min, prune and check inside the while 
                best_ans = min(best_ans, right - left + 1)

                # we remove the left to check if it's still a valid window, then increment the left
                window -= nums[left]
                left += 1

        return 0 if best_ans == float('inf') else best_ans
                