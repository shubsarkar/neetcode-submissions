# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # the leaf need to pass information back to parent to let them know, also the parent need to decide
        if not root:
            return None

        if root == p or root == q:
            return root

        left_scout = self.lowestCommonAncestor(root.left, p, q)
        right_scout = self.lowestCommonAncestor(root.right, p, q)

        if left_scout and right_scout:
            return root
        if left_scout:
            return left_scout
        if right_scout:
            return right_scout
        else:
            return None