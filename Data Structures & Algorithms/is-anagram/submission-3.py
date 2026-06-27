class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # count = {}
        # for char in s:
        #     count[char] = count.get(char, 0) + 1
        # for char in t:
        #     if char not in count or count[char] == 0:
        #         return False
        #     count[char] -= 1
        hash_1 = defaultdict(int)
        hash_2 = defaultdict(int)
        for i in range(len(s)):
            hash_1[s[i]] += 1
            hash_2[t[i]] += 1
        return hash_1 == hash_2