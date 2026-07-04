class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # this is a binary search problem with some limits
        # what are the limits -
        # ask about how much it can ship in a day min? max of the weights array and max would be all in 1 day
    
        min_limit = max(weights) # 10
        max_limit = sum(weights) # 26
        min_weight = 0

        # once I arrive at a number I will need to check it's feasibility

        while (min_limit <= max_limit):
            mid = min_limit + (max_limit - min_limit) // 2 # 1st mid: 18

            # now we try to see how many days does it take to meet 18 as weight limit
            summ, day_count = 0, 1

            for weight in weights:
                summ += weight
                if (summ > mid): # this would never trigger if every mid is larger than sum(weights)
                    day_count += 1
                    summ = weight # if we overshoot the last weight must be stored

            if day_count <= days:
                # we can do better! we want min, so we right shift
                min_weight = mid
                max_limit = mid - 1

            else:
                # we should be conservative
                min_limit = mid + 1
            
        return min_weight
