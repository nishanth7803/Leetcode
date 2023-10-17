class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        i, j = 0, len(s)-1
        while(i<=j):
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
