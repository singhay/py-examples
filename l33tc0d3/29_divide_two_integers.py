import sys
class Solution(object):
	def divide(self, dividend, divisor):
		positive = (dividend < 0) is (divisor < 0)
		dividend, divisor = abs(dividend), abs(divisor)
		quotient = 0
		while dividend >= divisor:
			temp, i = divisor, 1
			while dividend >= temp:
				# print(dividend, quotient, i, temp)
				dividend -= temp
				quotient += i
				i <<= 1
				temp <<= 1
				print(dividend, quotient, i, temp)
		if not positive:
			quotient = -quotient
		return min(max(-sys.maxsize-1, quotient), sys.maxsize)

x = Solution()
# print(x.divide(187, 7))

# print(x.divide(0, 1))
print(x.divide(-1, 1))
