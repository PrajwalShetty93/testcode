from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        leftnode = self.invertTree(root.left)
        rightnode = self.invertTree(root.right)
        root.right = leftnode
        root.left = rightnode
        return root



sol=Solution()

node =TreeNode(1)
node.left =TreeNode(2)
node.right =TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)


def print_tree(root):
    if not root:
        print("Empty tree")
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    print()

print_tree(node)
output = sol.invertTree(node)
print("Output")
print_tree(output)