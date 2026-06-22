class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        from collections import Counter
        count = Counter(nums)

        for item, count in count.items():
            if count > 1:
                return True

        return False





