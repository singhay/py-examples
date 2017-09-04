class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: bool
		"""
		if target in nums: return True
		for i in range(len(nums)-1):
			if nums[i+1] < nums[i]:
				pivot = i+1
				arr = nums[:pivot] if target > nums[0] else nums[pivot:]
				# print("pivot", nums[i+1], "index", i+1, "arr", arr)
				return self.binarySearch(arr, target)
		return False

	def binarySearch(self, arr, target):
		l, r = 0, len(arr)-1
		# print(l, r, target, arr)
		while l <= r:
			mid = (l+r)//2
			if target == arr[mid]:
				return True
			elif target < arr[mid]:
				r -= 1
			elif target > arr[mid]:
				l +=1
		return False

x = Solution()
print(x.search([], 2))
print(x.search([2], 2))
print(x.search([1,3,1], 2))
print(x.search([4,5,6,7,0,1,2], 2))
print(x.search([2,3,4,5,6,7,1], 2))
print(x.search([2,3,4,5,6,7,1], 9))
print(x.search([2,3,4,5,6,7,1], 5))