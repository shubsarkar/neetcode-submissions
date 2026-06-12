class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()
        left = 0 
        right = len(s) - 1

        while (left < right):
            if s[left] == s[right]:
                print(s[left], s[right])
                left += 1
                right -= 1
            else:
                return False
        
        return True