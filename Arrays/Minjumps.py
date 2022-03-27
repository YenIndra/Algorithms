def minJumps(self, arr, n):
      if n <= 1:
	        return 0
	    if arr[0] == 0:
	        return -1
	         
	    jumpidx = arr[0]
	    jumps = 1
	    steps = arr[0]
	    
	    
	    for i in range(1,n-1):
	        steps-=1
	        steps = max(steps,arr[i])
	        jumpidx -= 1
	        if jumpidx == 0:
	            jumpidx = steps
	            jumps+=1
	        if jumpidx <= 0:
	            return -1
	    return jumps
