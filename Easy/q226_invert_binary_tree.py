class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


solution = Solution()
treeNode = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(
    3, None, None)), TreeNode(7, TreeNode(6, None, None), TreeNode(9, None, None)))

solution.invertTree(treeNode)
