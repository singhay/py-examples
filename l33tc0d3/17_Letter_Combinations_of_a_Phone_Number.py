class Solution(object):
	keypad = {	'2':['a','b','c'], 
				'3':['d','e','f'],
				'4':['g','h','i'],
				'5':['j','k','l'],
				'6':['m','n','o'],
				'7':['p','q','r','s'],
				'8':['t','u','v'],
				'9':['w','x','y','z'] }

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		:input: "23"
		:output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
		"""
		dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
		return [a+b for a in dic.get(digits[:1],'') for b in self.letterCombinations(digits[1:]) or ['']] or []

	def letterCombinationsBackTrack(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		:input: "23"
		:output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
		"""
		output = []
		# for digit in digits:
		if digits=="": return []
		for letter in self.keypad[digits[0]]:
			# print(letter, digits, output)
			output += [letter + c for c in self.letterCombinations(digits[1:]) or [""]]

		return output

x = Solution()
print(x.letterCombinations(""))
print(x.letterCombinations("23"))


