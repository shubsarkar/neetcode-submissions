class Solution:
    def validPalindrome(self, s: str) -> bool:
        # we get one skip

        def checkPalindrome(left, right):
            while(left < right):
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        # main loop to check if palindrome
        left, right = 0, len(s) - 1
        while (left < right):
            if s[left] != s[right]:
                # one skip we can afford need to check if left or right part after deleting one is valid
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)

            left += 1
            right -= 1

        return True
