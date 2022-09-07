def isStackPermutation(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        stack = [] # Declared stack for stack operations
        i,j = 0,0 # Counters for A and B
        
        while(i < N and j < N):
            while(stack and stack[-1] == B[j]):
                stack.pop()
                j+=1
            stack.append(A[i])
            i+=1
        #print(stack)
        while(stack and j<N and stack[-1] == B[j]):
                #print('Before ',j)
                stack.pop()
                j+=1
                #print(j)
                
                
        if stack:
            return 0
        else:
            return 1
