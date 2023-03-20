# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def inorder(node, intList) -> list:
            if node:
                intList = inorder(node.left, intList)
                intList.append(node.val)
                intList = inorder(node.right, intList)
            return intList
        
        intList = []
        inorder(root, intList)
        return intList