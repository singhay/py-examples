class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val, left=None, right=None):
		super(TreeNode, self).__init__()
		self.val = val
		self.left = left
		self.right = right
		
	def print(self, head):
		if head:
			print(head.val)
			self.print(head.left)
			self.print(head.right)


class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""
		if not t1 and not t2: return None
		ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
		ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
		ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
		return ans


t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
# t1.print()
t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
# t2.print(t2)
s = Solution()
t = s.mergeTrees(t1, t2)
t.print(t)
