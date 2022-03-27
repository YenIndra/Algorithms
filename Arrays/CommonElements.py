def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        ls = list(set(A) & set(B) & set(C))
        return sorted(ls)
        
