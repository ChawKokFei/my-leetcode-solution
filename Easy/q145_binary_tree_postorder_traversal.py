# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        def postorder(node, intList) -> list:
            if node:
                intList = postorder(node.left, intList)
                intList = postorder(node.right, intList)
                intList.append(node.val)
            return intList

        intList = []
        postorder(root, intList)
        return intList