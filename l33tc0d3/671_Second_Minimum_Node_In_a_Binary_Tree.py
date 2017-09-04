class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val, left=None, right=None):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	"""docstring for Solution"""
	def findSecondMinimumValue(self, root):
		mix = [float('inf')]
		def findAllNodes(head):
			if not head: return
			if root.val < head.val < mix[0]:
				mix[0] = head.val
			findAllNodes(head.left)
			findAllNodes(head.right)
		findAllNodes(root)
		return mix[0] if mix[0] != float('inf') else -1



# t = TreeNode(5, TreeNode(3, None, TreeNode(4)), TreeNode(6, None, TreeNode(7)))
# t = TreeNode(2, TreeNode(2), TreeNode(2))
t = TreeNode(5, TreeNode(8), TreeNode(5))
s = Solution()
print(s.findSecondMinimumValue(t))
		