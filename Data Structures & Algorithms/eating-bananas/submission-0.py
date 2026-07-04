class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) # koko must eat atleast 1, max is something she will eat if she has to finish the entire pile in # of elements hours
        # 1 , 4
        result = 0
        while (left <= right):
            mid = left + (right - left) // 2 # 2

            # we now check with value of 2 to see if we can eat all piles in given h hours or not
            # if the pile has >k bananas, finish pile, can't touch another pile
            hours, k_count = 0, 0
            for nums in piles:
                hours += math.ceil(nums/mid)
            
            if hours <= h:
                # this is possible scenario
                right = mid - 1
            else:
                left = mid + 1

        return left
