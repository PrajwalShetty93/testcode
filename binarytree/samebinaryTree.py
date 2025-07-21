# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list1=[]
        list2=[]

        def dfs(root,testList):
            if root is None:
                testList.append(None)
                return None
            
            left = dfs(root.left,testList)
            right = dfs(root.right,testList)
            testList.append(root.val)
            

        dfs(p,list1)
        dfs(q,list2)

        if list1 ==list2:
            return True
        return False

root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

root1 = TreeNode(1)
root1.left=TreeNode(2)
root1.right=TreeNode(3)
# root1.right.left=TreeNode(4)
sol=Solution()
print(sol.isSameTree(root,root1))