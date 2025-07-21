from typing import Optional


#       1
#      / \
#     2   3
#    / \
#   4   5

class TreeNode:

    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.result = 0


#       1
#        \
#         2
#        / \
#       3   4
#      /
#     5

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        print(root.val)

        leftHeight = self.diameterOfBinaryTree(root.left)
        rightHeight = self.diameterOfBinaryTree(root.right)
        height = 1+ max(leftHeight,rightHeight)
        print('height:',height)
        diameter = leftHeight+rightHeight
        print('diameter:',diameter)
        self.result = max(self.result,diameter)
        print('result:',self.result)
        return height
    

    def diameterOfBinaryTree_2(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        def internalfunction(root):
            if root is None:
                return 0
            print(root.val)

            leftHeight = internalfunction(root.left)
            rightHeight = internalfunction(root.right)
            height = 1+ max(leftHeight,rightHeight)
            print('height:',height)
            diameter = leftHeight+rightHeight
            print('diameter:',diameter)
            self.res = max(self.res,diameter)
            print('res:',self.res)
            return height
        
        internalfunction(root)
        return self.res
        
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(5)
sol=Solution()
height = sol.diameterOfBinaryTree(root)
print(height)
print(sol.result)

# This is similar to height of the binary tree. But apart from calculating the height, we need to calculate the diameter
# which is leftheight+rightHeight and we will be saving this in a variable result. Now result is a class variable which is used 
# externally from the fucntion. There are 2 ways to achieve this: One is above, other is below: