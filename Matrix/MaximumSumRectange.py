class Solution:
    def kadane(self,arr,c):
        res = -99999999999
        sm = 0
        for i in range(c):
            sm+=arr[i]
            if sm > res:
                res = sm
            if sm <0:
                sm = 0
        return res
    
    def maximumSumRectangle(self,R,C,M):
        #code here
        res = -99999999999
        for i in range(R):
            temp = [0]*C
            for j in range(i,R):
                for col in range(C):
                    temp[col]+=M[j][col]
                ans = self.kadane(temp,C)
                res = max(ans,res)
                
        return res
