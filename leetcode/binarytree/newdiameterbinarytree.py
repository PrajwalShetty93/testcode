from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#       1
#        \
#         2
#        / \
#       3   4
#      /
#     5        

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def internalFunction(root):
        
            if not root:
                return 0
            

            leftHeight =  internalFunction(root.left)
            rightHeight =  internalFunction(root.right)
            
            height = 1+max(leftHeight,rightHeight)
            diameter = leftHeight+rightHeight
            self.res = max(diameter,self.res)
            
            return height
        
        internalFunction(root)
        return self.res



sol=Solution()

node =TreeNode(1)
node.right =TreeNode(2)
node.right.left = TreeNode(3)
node.right.right = TreeNode(4)
node.right.left.left = TreeNode(5)

res = sol.diameterOfBinaryTree(node)
print(res)
