class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        print(a.sort(), b.sort())
        if a == b:
            return True
        return False