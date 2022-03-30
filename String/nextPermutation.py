def nextPermutation(self, N, arr):
        # code here
        k = -1
        l = 0
        i = N -1
        while(i>0):
            if arr[i-1] < arr[i]:
                k = i-1
                break
            i-=1
        if k == -1:
            return arr[::-1]
        i = N-1
        while(i>k):
            if arr[i] > arr[k]:
                l = i
                break
            i-=1
        arr[l],arr[k] = arr[k],arr[l]
        
        newarr = arr[0:k+1] + arr[k+1:][::-1]
        #print(newarr)
        return newarr
