class TreeNode:

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node: TreeNode = TreeNode(val=val)
        if root == None:
            root = node
            return root

        current: TreeNode = root
        while True:
            if val < current.val:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right

        return root

