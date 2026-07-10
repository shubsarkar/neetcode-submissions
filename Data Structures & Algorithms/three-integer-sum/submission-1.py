class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if I fix one number and apply two sum over i+1 till the end?

        # sort so that duplicates are adjacent and the sum is monotonic
        nums.sort()
        n = len(nums)
        results = []

        # fix an anchor i, then two-pointer sweep on (i+1, n-1)
        for i in range(n-2):
            # early termination - smallest element is already positive
            if nums[i] > 0:
                break

            # skip the repeated numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, n - 1
            target = -nums[i]

            while (left < right):
               
                s = nums[left] + nums[right]

                if s == target:
                    results.append([nums[i], nums[left], nums[right]])
        
                    left += 1
                    right -= 1

                    # skip repeated values on both sides
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -=1
                    
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return results

        