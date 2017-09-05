import re

class Solution:
	# re.match('.*[a-zA-Z0-9].*', yourstring)
	# re.match('^0[1-7][0-7]*$', yourstring)
	def parseInt(self, str):
		str = str.strip()
		if ((str == '0x' or str == '-0x') and str[2].isdigit()) or str.startswith('0x') or str.startswith('-0x'): 
			return int(str, 16)
		elif str[0].isdigit() or (str[0] == '-' and str[1].isdigit()):
			return int("".join([i for i in str if i.isdigit()]))

x = Solution()
print(x.parseInt("123"))
print(x.parseInt("123 -"))
print(x.parseInt("123abc"))
print(x.parseInt("0x20"))
print(x.parseInt("-0x20"))
# print(x.parseInt("0x"))
print(x.parseInt("a123"))
print(x.parseInt("1 23"))
print(x.parseInt("-2"))
print(x.parseInt("--2"))
print(x.parseInt("+2"))
print(x.parseInt("\t  \n 2"))
print(x.parseInt("0002"))