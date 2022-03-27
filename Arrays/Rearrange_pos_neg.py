def rearrange(self,arr, n):
        # code here
        posarr = []
        negarr = []
        for i in arr:
            if i < 0:
                negarr.append(i)
            else:
                posarr.append(i)
        
        #print(posarr)
        #print(negarr)
        i = 0
        j = 0
        cycle = 0
        res = []
        while i < len(posarr) and j < len(negarr):
            if cycle % 2 == 0:
                res.append(posarr[i])
                i+=1
            else:
                res.append(negarr[j])
                j+=1
            cycle+=1
        #print("1 = ",res)
        while i < len(posarr):
            res.append(posarr[i])
            i+=1
        #print("2 = ",res)    
        while j < len(negarr):
            res.append(negarr[j])
            j+=1
        #print("3 = ",res)    
        
        arr.clear()
        for i in range(n):
            arr.append(res[i])
