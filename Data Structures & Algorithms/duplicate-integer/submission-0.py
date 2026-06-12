class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter

        counter_dup = Counter(nums)

        for item, count in counter_dup.items():
            if count > 1:
                return True

        return False

