# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]

# Definition for a binary tree node.

#       1
#      / \
#     2   3
#    / \
#   4   5

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            
            self.inorder(root.left)
            
            self.inorder(root.right)
            print(root.val,' ')

#       1
#      / \
#     2   3
#    / \
#   4   5


    def treeSum(self, root: Optional[TreeNode]):
        if not root:
            return 0
        # print(root.val)
        
        leftSum = self.treeSum(root.left)    
        # print(leftSum)
        rightSum = self.treeSum(root.right)  
        # print(rightSum)
        return root.val+leftSum+rightSum     
    
    def treeMax(self,root):
        if not root:
            return float("-inf")
        
        leftMax = self.treeMax(root.left)
        rightMax = self.treeMax(root.right)
        return max(root.val,leftMax,rightMax)
    
    def treeHeight(self,root):
        if not root:
            return 0
        print(root.val)
        leftHeight = self.treeHeight(root.left)
        rightReight = self.treeHeight(root.right)
        return 1+ max(leftHeight,rightReight)   
    
    # This is slighly tricky, as the max height, we dont have to add the values of the node, just add 1


#       1
#      / \
#     2   3
#    / \
#   4   5

    def invertBinaryTree(self,root):
        if not root:
            return None
        print(root.val)


        left_node = self.invertBinaryTree(root.left)
        right_node = self.invertBinaryTree(root.right)
        root.left=right_node
        root.right=left_node
        return root




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol=Solution()
sol.inorder(root)
# print(sol.treeSum(root))
# print(sol.treeMax(root))
# print(sol.treeHeight(root))
sol.invertBinaryTree(root)

