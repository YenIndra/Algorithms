import sys
class Solution:
	def solveWordWrap(self, nums, k):
		#Code here
		n = len(nums)
		dp = [0]*n
		dp[n-1] = 0
		for i in range(n-2,-1,-1):
		    currlen = -1
		    dp[i] = sys.maxsize
		    for j in range(i,n):
		        currlen += nums[j]+1
		        if currlen > k:
		            break
		        if j == n-1:
		            cost = 0
		        else:
		            cost = (k-currlen)*(k-currlen) + dp[j+1]
		        dp[i] = min(dp[i],cost)
		       
		return dp[0] 
