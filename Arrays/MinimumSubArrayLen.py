def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = 10 ** 6
        s = target
        left = 0
        summ = 0
        for i in range(n):
            summ+=nums[i]
            while summ >= s:
                ans = min(ans, i - left + 1)
                summ-= nums[left]
                left+=1
        return ans if ans != 10 ** 6 else 0
        
