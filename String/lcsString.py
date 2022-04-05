def lcs(self,x,y,s1,s2):
        
        # code here
        l = [[0]*(y+1) for _ in range(x+1)]
        for i in range(x):
            for j in range(y):
                if s1[i] == s2[j]:
                    l[i][j] = l[i-1][j-1]+1
                else:
                    l[i][j] = max(l[i][j-1],l[i-1][j])
        return l[x-1][y-1]
