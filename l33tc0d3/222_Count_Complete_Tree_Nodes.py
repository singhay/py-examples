# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftDepth = self.leftDepth(root)
        rightDepth = self.rightDepth(root)
        if leftDepth == rightDepth:
            # print(leftDepth, rightDepth, (1 << leftDepth) - 1)
            return (1 << leftDepth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def leftDepth(self, root):
        l = 0
        while root is not None:
            print("LEFT", root.val)
            root = root.left
            l+=1
        return l

    def rightDepth(self, root):
        l = 0
        while root is not None:
            print("RIGHT", root.val)
            root = root.right
            l+=1
        return l


node1 = TreeNode(2)
node1.left = TreeNode(1)
node1.right = TreeNode(3)
node2 = TreeNode(6)
node2.left = node1
node2.right = TreeNode(8)
node3 = TreeNode(3)
node3.left = TreeNode(2)
node3.right = TreeNode(4)
node = TreeNode(5)
node.left = node3
node.right = node2

x = Solution()
print(x.countNodes(node))