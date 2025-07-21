# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

#       1
#      / \
#     2   3
#          \
#           4


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.max_length_diff=0

        def internal_function(root):
            if root is None:
                return 0
        
            leftHeight = internal_function(root.left)
            rightHeight = internal_function(root.right)
            height = 1+ max(leftHeight,rightHeight)
            self.max_length_diff=max(self.max_length_diff,(abs(leftHeight-rightHeight)))
            return height

        internal_function(root)
        if self.max_length_diff>1:
            return False
        return True   

sol=Solution()
root = TreeNode(1)
root.left=TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
result = sol.isBalanced(root)
print(result)