def find3Numbers(self,A, n, X):
        # Your Code Here
        A.sort()
        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                reqsum = A[i] + A[l] + A[r]
                if reqsum == X:
                    return True
                elif reqsum < X:
                    l+=1
                else:
                    r-=1
                    
        return False
