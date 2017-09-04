# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		prev = None
		while head:
		    curr = head
		    head = head.next
		    curr.next = prev
		    prev = curr
		return prev

	def print(self, head):
		while head:
			print(head.val)
			head = head.next



node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5


x = Solution()
x.print(node1)
x.print(x.reverseList(node1))