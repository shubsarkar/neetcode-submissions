class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        major_cnt = 1

        for i in range(1, len(nums)):

            if major_cnt == 0:
                element = nums[i]
            if nums[i] == element:
                major_cnt += 1
            else:
                major_cnt -= 1

        return element            
