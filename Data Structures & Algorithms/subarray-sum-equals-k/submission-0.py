class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # have a hashmap which stores the prefix sum and count, so that when you traverse down you know when that sum was encountered.
        # k - sum, would reveal what other part of the sum is required. 

        prefix = 0
        count = 0
        mp = {0:1}

        for num in nums:
            # have id and the element
            prefix += num

            # check if k - prefix exists in the mp or not
            if (prefix-k) in mp:
                # if this exists we know we have a subarray equating to k
                count += mp[prefix-k]
            
            mp[prefix] = mp.get(prefix, 0) + 1

        return count

            