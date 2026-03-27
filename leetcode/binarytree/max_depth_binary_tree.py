
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        return 1 + max(leftMax,rightMax)
        


sol=Solution()

node =TreeNode(1)
node.left =TreeNode(2)
node.right =TreeNode(3)
node.right.left = TreeNode(4)

res = sol.maxDepth(node)
print(res)

