def countPs(self,string):
        # Code here
        N = len(string)
 
    
        cps = [[0 for i in range(N + 2)]for j in range(N + 2)]
 
        # palindromic subsequence of length 1
        for i in range(N):
            cps[i][i] = 1
        #print(cps)
    
        for L in range(2, N + 1):
 
            for i in range(N):
                k = L + i - 1
                if (k < N):
                    if (string[i] == string[k]):
                        cps[i][k] = (cps[i][k - 1] +
                                    cps[i + 1][k] + 1) % (10 ** 9 + 7)
                    else:
                        cps[i][k] = (cps[i][k - 1] +
                                    cps[i + 1][k] -
                                    cps[i + 1][k - 1]) % (10 ** 9 + 7)
 
    # return total palindromic subsequence
        #print(cps)
        return cps[0][N - 1]
