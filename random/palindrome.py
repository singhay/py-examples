def palindrome(s):
	p = True
	for i in range(len(s)//2):
		if s[i]==s[(i*-1)-1] and p: p = True
		else: p = False

	return p

print(palindrome("abba"))