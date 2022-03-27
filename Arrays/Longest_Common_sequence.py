def findLongestConseqSubseq(self,arr, N):
        #code here
        s = set()
        res = 0
        for i in arr:
            s.add(i)
        for i in range(N):
            if (arr[i] - 1) not in s:
                j = arr[i]
                while j in s:
                    j+=1
                res = max(res,j-arr[i])
        return res
