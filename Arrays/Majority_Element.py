 def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        numCounts = Counter(nums)
        ans = []
        k = len(nums)//3
    
        for i in numCounts:
            if numCounts[i] > k:
                ans.append(i)
        return ans
