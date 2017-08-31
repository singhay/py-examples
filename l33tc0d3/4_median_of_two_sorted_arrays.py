class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		"""
		Naive Solution
		nums = sorted(nums1+nums2)
		return ((nums[(len(nums)//2)-1]+nums[len(nums)//2])/2.) if len(nums)%2==0 else nums[len(nums)//2]
		"""
		 # to make sure a1 is always the longest array among the two
		if len(nums1)>=len(nums2):
			a1, a2 = nums1, nums2
		else:
			a1, a2 = nums2, nums1
		i = []
		for num in a2:
			a1.insert(self.findNumber(a1, num), num)
		return ((a1[(len(a1)//2)-1]+a1[len(a1)//2])/2.) if len(a1)%2==0 else a1[len(a1)//2]
			

	def findNumber(self, arr, num):
		"""
		Returns index of a number if present else -1
		:type arr: List[int]
		:type num: List[int]
		:rtype: int
		"""
		if num < arr[0]:
			return 0
		if num > arr[-1]:
			return len(arr)
		left = 0
		right = len(arr)-1
		while left <= right:
			mid = (left + right)//2
			if num <= arr[mid] and num >= arr[mid-1]:
				return mid
			elif num < arr[mid]:
				right = mid-1
			elif num > arr[mid]:
				left = mid+1 


x = Solution()
# print(x.findMedianSortedArrays([1,3,5,7,9], [2,4,6]))
print(x.findMedianSortedArrays([1,3], [0,2]))
"""
assert x.findMedianSortedArrays([1,3], [2]) == 2
assert x.findMedianSortedArrays([2], [1,3]) == 2
assert x.findMedianSortedArrays([1,3], [4]) == 3
assert x.findMedianSortedArrays([4], [1,3]) == 3
"""