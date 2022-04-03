#User function Template for python3

class Solution:
    def search2D(self,grid,row,col,word):
        dir = [[-1,0],[1,0],[1,1],[1,-1],[-1,-1],
                [-1,1],[0,1],[0,-1]]
        if grid[row][col] != word[0]:
            return False
        R,C = len(grid),len(grid[0])
        
        for r,c in dir:
            newr = row + r
            newc = col + c
            flag = True
            for k in range(1,len(word)):
                if( 0<= newr < R and 0<= newc < C and word[k] == grid[newr][newc]):
                    newr+=r
                    newc+=c
                else:
                    flag = False
                    break
            if flag:
                return True
        return False
        
	def searchWord(self, grid, word):
		# Code here
		R = len(grid)
		C = len(grid[0])
		ans = []
		for row in range(R):
		    for col in range(C):
		        if self.search2D(grid,row,col,word):
		            ans.append([row,col])
		            
	    r
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends
