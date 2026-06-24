class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can maintain a set to uniquely identify which elements are present

        set_of_nums = set(nums) # we can look up when we require to  (2, 20, 4, 10, 3, 4, 5) for O(1) lookup

        # we need to track the min - start of the sequence, we know it's the min when val - 1 is not present in the array

        longest = 0
        # [2, 20, 4, 10, 3, 4, 5] 
        for num in nums:  # 2 gets processed
            if num - 1 not in set_of_nums:
                # we know that we have found a probable start point
                length = 1
                while(num + length) in set_of_nums:
                    length += 1

                longest = max(length, longest)

        return longest
                


