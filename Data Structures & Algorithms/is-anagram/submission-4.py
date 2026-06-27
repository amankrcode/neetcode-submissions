class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_1 = defaultdict(int)
        hash_2 = defaultdict(int)
        for i in range(len(s)):
            hash_1[s[i]] += 1
            hash_2[t[i]] += 1
        return hash_1 == hash_2