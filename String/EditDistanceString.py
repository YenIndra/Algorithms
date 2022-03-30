def editDistance(self, s, t):
		# Code here
		n = len(s)
		m = len(t)
		dp = [[0 for x in range(m+1)] for _ in range(n+1)]
		for i in range(n+1):
		    for j in range(m+1):
		        if i == 0:
		            dp[i][j] = j
		        if j == 0:
		            dp[i][j] = i
		            
	    for i in range(1,n+1):
	        for j in range(1,m+1):
	            if s[i-1] == t[j-1]:
	                dp[i][j] = dp[i-1][j-1]
	            else:
	                dp[i][j] = 1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
	                
	    return dp[n][m]
