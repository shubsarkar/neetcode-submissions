# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1   # 0 
        right = n  # 15

        while left <= right:   # 0 <= 15
            mid = left + (right - left) // 2 # 7
            result = guess(mid) # 0, -1, 1, eg. 7
            
            if result == 0: 
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1

        return mid