class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n 
        # if I use two pointers, one starting at kth step?
        def reverse_two(left, right):
            while (left < right):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse_two(0, n - 1)
        reverse_two(0, k - 1)
        reverse_two(k, n - 1)

        # [1,2,3,4,5,6,7,8], k = 4
        # [8,7,6,5,4,3,2,1] -- reverse the entire array
        # [5,6,7,8,4,3,2,1] -- reverse the first k
        # [5,6,7,8,1,2,3,4] -- reverse k+1 to n

        
