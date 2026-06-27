class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for x in s:
            if x.isalnum():
                newstr += x.lower()
        return newstr == newstr[::-1]