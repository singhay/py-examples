class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		x = str(numerator/denominator);
		whol, dec = '', ''
		if '.' in x:
			whol, dec = x.split('.')
			# print(whol, dec)
			if len(dec)>1:
				dec = self.compressRecurring([s for s in dec], 0)
			# print(whol, dec)
		return ".".join([whol, dec])

	def compressRecurring(self, dec, prev):
		# print(dec, prev)
		if len(dec) <= 2:
			return dec[0]
		if dec[prev] == dec[prev+1]:
			return self.compressRecurring(dec[prev+1:], prev)
		else:
			return self.compressRecurring(dec[prev:], prev+1)

x = Solution()
# print(x.fractionToDecimal(10, 3))
# print(x.fractionToDecimal(10, 2))
# print(x.fractionToDecimal(1, 3))
# print(x.fractionToDecimal(1, 2))
# print(x.fractionToDecimal(1, 5))
print(x.fractionToDecimal(1, 512))