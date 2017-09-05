from random import randint

class Sort(object):
	"""docstring for Sort"""
	def __init__(self):
		super(Sort, self).__init__()

	def mergeSort(self, arr):
		def merge(left, right):
			i, j, res = 0, 0, []
			while i<len(left) and j<len(right):
				if left[i] <= right[j]: 
					res.append(left[i])
					i += 1
				else:
					res.append(right[j])
					j += 1
			return res + left[i:] + right[j:]

		if len(arr) < 2: return arr
		m = len(arr)//2
		return merge(self.mergeSort(arr[:m]), self.mergeSort(arr[m:]))


	def quickSortQuadratic(self, arr):
		"""
		This version is not In place
		"""
		if len(arr)<2: return arr
		return  self.quickSort([x for x in arr[1:] if x<arr[0]]) + \
				[arr[0]] + \
				self.quickSort([x for x in arr[1:] if x>=arr[0]])


	# Quicksort with starting index as pivot
	def qsortFirstElemPivot(self, items):
	  if len(items) < 2:
	    return items
	  pivot = items[0]
	  left = list(filter(lambda x: x <= pivot, items[1:]))
	  right = list(filter(lambda x: x > pivot, items[1:]))
	  return qsort(left) + [pivot] + qsort(right)

	# Quicksort implemented with a random pivot
	def quickSort(self, items):
	  if len(items) < 2: return items
	  p_i = randint(0, len(items) - 1)
	  nonPivArr = items[:p_i] + items[p_i + 1:]
	  pivot = items[p_i]
	  left = list(filter(lambda x: x <= pivot, nonPivArr))
	  right = list(filter(lambda x: x > pivot, nonPivArr))
	  return self.quickSort(left) + [pivot] + self.quickSort(right)
		



x = Sort()
# print(x.mergeSort([20, 7, 3, 4, 12, 15, 2, 1]))
# print(x.mergeSort([1]))
# print(x.mergeSort([]))
print(x.quickSort([20, 7, 3, 4, 12, 15, 2, 1]))
# print(x.quickSort([1]))
# print(x.quickSort([]))
# print(x.quickSort())


def merge(lrr, rrr):
	if len(rrr)>len(lrr): lrr, rrr = rrr, lrr
	j = 0
	print("MERGING", lrr, rrr)
	for i in range(len(rrr)):
		while lrr[j] < rrr[i]: 
			j += 1
		print(lrr[:j], [rrr[i]], lrr[j:])
		lrr = lrr[:j] + [rrr[i]] + lrr[j:]
	return lrr

# print(merge([20], [7]))
# print(merge([3], [4]))
# print(merge([1, 3, 4, 7, 20], [1, 2, 12, 15]))