class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        # let's maintain a seen set, that will track the window
        seen = set()
        best_ans = 0

        for right in range(len(s)):
            # we need to check if it's part of the set first
            while s[right] in seen:
                # the window is flawed now, contains repeating characters and we want the longest so we need to fix the window first
                seen.remove(s[left])
                left += 1

            # at this point it's safe to update the window with the new element
            seen.add(s[right])

            # update the longest
            best_ans = max(best_ans, right - left + 1)

        return best_ans
