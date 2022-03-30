 def longestPalin(self, S):
        # code here
        n = len(S)
        if n < 2:
            return S
        start = 0
        maxlen = 1
        for i in range(n):
            low = i-1
            high = i+1
            while high < n and S[high] == S[i]:
                high+=1
            while low >=0 and S[low] == S[i]:
                low-=1
            while low>=0 and high <n and S[high] == S[low]:
                high+=1
                low-=1
            l = high - low -1
            if l > maxlen:
                maxlen = l
                start = low+1
                
        return S[start:start+maxlen]
