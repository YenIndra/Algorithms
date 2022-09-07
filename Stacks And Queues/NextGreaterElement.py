def nextLargerElement(self,arr,n):
        #code here
        stack = []
        ans = [-1]
        
        stack.append(arr[-1])
        for i in range(n-2,-1,-1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
                
            stack.append(arr[i])
            
        return ans[::-1]
