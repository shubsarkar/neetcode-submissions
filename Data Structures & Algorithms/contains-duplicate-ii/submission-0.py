class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # store the values and indexes in a dict
        # val : a1, when you find a duplicate check if it's in the k vicinity

        track = {}

        for idx, num in enumerate(nums):
            if num in track:
                if abs(idx - track[num]) <= k:
                    return True
            track[num] = idx

        return False    