class Solution(object):
	def threeSumBruteForce(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		PASSES 240 CASES, TLE TIME LIMIT EXCEEDS
		"""
		ans = []
		for a in nums:
			t = nums[:]
			t.remove(a)
			for b in t:
				x = t[:]
				x.remove(b)
				for c in x:
					if a+b+c==0 and sorted([a,b,c]) not in ans:
						ans += [sorted([a,b,c])]
		return ans


	def threeSumDP(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		WIP
		"""
		if nums == []: return nums
		if sum(c)==0 and len(c)==3: return c

		print(k)
		for a in nums:
			triplt = [a]+c
			if triplt in k.keys(): return k[triplt]
			if sum(triplt)==0 and len(triplt)==3: return triplt
			t = nums[:]
			t.remove(a)
			return [self.threeSum(t, [a]+c, k), self.threeSum(t, c, k)]


	def threeSum(self, nums):
		res = []
		nums.sort()
		for i in range(len(nums)-2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			l, r = i+1, len(nums)-1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				if s < 0:
					l +=1 
				elif s > 0:
					r -= 1
				else:
					res.append((nums[i], nums[l], nums[r]))
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
					l += 1; r -= 1
		return res

	
x = Solution()
print(x.threeSum([0,0]))
print(x.threeSum([0,0,0]))
print(x.threeSum([1,2,-2,-1]))
print(x.threeSum([-1, 0, 1, 2, -1, -4]))
print(x.threeSum([3,0,-2,-1,1,2]))
print(x.threeSum([-5,0,-2,3,-2,1,1,3,0,-5,3,3,0,-1]))
print(x.threeSum([3,-9,3,9,-6,-1,-2,8,6,-7,-14,-15,-7,5,2,-7,-4,2,-12,-7,-1,-2,1,-15,-13,-4,0,-9,-11,7,4,7,13,14,-7,-8,-1,-2,7,-10,-2,1,-10,6,-9,-1,14,2,-13,9,10,-7,-8,-4,-14,-5,-1,1,1,4,-15,13,-12,13,12,-11,12,-12,2,-3,-7,-14,13,-9,7,-11,5,-1,-2,-1,-7,-7,0,-7,-4,1,3,3,9,11,14,10,1,-13,8,-9,13,-2,-6,1,10,-5,-6,0,1,8,4,13,14,9,-2,-15,-13]))