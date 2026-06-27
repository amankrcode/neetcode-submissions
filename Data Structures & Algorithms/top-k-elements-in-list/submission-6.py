class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter dictionary
        count={}
        arr = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # arrange value with frequency
        for num, cnt in count.items():
            arr.append([cnt, num])
        # sort in ascending order
        arr.sort()
        res = []
        
        while len(res) < k:
            res.append(arr.pop()[1])
        return res