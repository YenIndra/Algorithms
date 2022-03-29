class Solution:
    def maxHist(self,row):
        stack = []
        tp = 0
        mx_area = 0
        area = 0
        i =0
        while(i < len(row)):
            if (len(stack) == 0) or (row[stack[-1]] <= row[i]):
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                area = row[tp] * ((i-stack[-1]-1) if stack else i)
                mx_area = max(area,mx_area)
            
                
        while(stack):
            tp = stack.pop()
            area = row[tp] * ((i-stack[-1]-1) if stack else i)
            mx_area = max(area,mx_area)
        return mx_area
        
        
        
    def maxArea(self,M, n, m):
        # code here
        maxRect = self.maxHist(M[0])
        for i in range(1,n):
            for j in range(m):
                if M[i][j]:
                    M[i][j]+=M[i-1][j]
                    
            temp = self.maxHist(M[i])
            maxRect = max(maxRect,temp)
            
        return maxRect
