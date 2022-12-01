def palindromeIndex(s):
	# Write your code here
	s = list(s)
	for i in range(len(s)//2):
		if s[i] != s[-(i+1)]:
			new_list = s[:i] + s[i+1:]
			if(isPalindrome(new_list)):
				return i
			else:
				return len(s)-1-i
		return -1
def isPalindrome(s):
	return s == s[::-1]
