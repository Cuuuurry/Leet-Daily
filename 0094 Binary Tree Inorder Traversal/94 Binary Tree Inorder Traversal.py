from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        self.inorderpath(root, res)
        return res

    def inorderpath(self, root, path):
        if root.left:
            self.inorderpath(root.left, path)
        path.append(root.val)
        if root.right:
            self.inorderpath(root.right, path)
        return path
