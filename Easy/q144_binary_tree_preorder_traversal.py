# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        def preorder(node, intList) -> list:
            if node:
                intList.append(node.val)
                intList = preorder(node.left, intList)
                intList = preorder(node.right, intList)
            return intList

        intList = []
        preorder(root, intList)
        return intList