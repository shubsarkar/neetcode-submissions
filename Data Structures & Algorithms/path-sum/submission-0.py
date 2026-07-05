# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False # empty node can't equate to target

        # step 2 - pre order login & leaf check
        if root.left is None and root.right is None:
            # we have a leaf cell
            if root.val == targetSum or root.val == targetSum:
                return True


        # recursive leap - pass the updated target down to the children
        left_found = self.hasPathSum(root.left, targetSum - root.val)
        right_found = self.hasPathSum(root.right, targetSum - root.val)

        return left_found or right_found