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
		def findSecondMinimumValueR(root):
			mi = []
			if root:
				mi = findSecondMinimumValueR(root.left) + [root.val] + findSecondMinimumValueR(root.right)
			# x = sorted()
			return mi
		mi = set(sorted(findSecondMinimumValueR(root)))
		print(mi)
		return mi[1] if len(mi)>1 else -1




# t = TreeNode(5, TreeNode(3, None, TreeNode(4)), TreeNode(6, None, TreeNode(7)))
# t = TreeNode(2, TreeNode(2), TreeNode(2))
t = TreeNode(5, TreeNode(8), TreeNode(5))
s = Solution()
print(s.findSecondMinimumValue(t))
		