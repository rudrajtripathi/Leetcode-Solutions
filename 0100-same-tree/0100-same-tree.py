# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Case 1: Both nodes are empty
        if p is None and q is None:
            return True

        # Case 2: Only one node is empty
        if p is None or q is None:
            return False

        # Case 3: Values are different
        if p.val != q.val:
            return False

        # Check both left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))