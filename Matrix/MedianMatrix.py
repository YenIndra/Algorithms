def median(self, matrix, r, c):
    	#code here 
    	mi = matrix[0][0]
    	mx = 0
    	for i in range(r):
    	    if matrix[i][0] < mi:
    	        mi = matrix[i][0]
    	    if matrix[i][c-1] > mx:
    	        mx = matrix[i][c-1]
    	desired = (r*c+1)//2
    	while (mi < mx):
    	    mid = mi + (mx-mi)//2
    	    #print("mid = ",mid)
    	    place = 0
    	    for i in range(r):
    	        j = bisect_right(matrix[i],mid)
    	        place+=j
    	       
            if place < desired:
                mi = mid+1
                #print("min = ",mi)
            else:
                mx = mid
                #print("mx = ",mx)
                
        return mi
