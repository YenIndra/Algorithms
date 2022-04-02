

class Solution:
	def lps(self, s):
		# code here
		n = len(s)
		lsp = [0] * n
		l = 0
		
		i = 1
		while i < n:
	        if s[i] == s[l]:
	            l+=1
	            lsp[i] = l
	            i+=1
	        else:
	            if l!=0:
	                l = lsp[l-1]
	            else:
	                lsp[i] = 0
	                i+=1
        return lsp[n-1]
		    
	    return len(ls)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends
