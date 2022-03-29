def spirallyTraverse(self,matrix, r, c): 
        # code here 
        top,down,left,right = 0,r,0,c
        dir = 0
        ans = []
        while (top < down) and (left < right):
            if dir == 0:
                for i in range(left,right):
                    ans.append(matrix[top][i])
                top+=1
            elif dir == 1:
                for i in range(top,down):
                    ans.append(matrix[i][right-1])
                right-=1
            elif dir == 2:
                for i in range(right-1,left-1,-1):
                    ans.append(matrix[down-1][i])
                down-=1
            elif dir == 3:
                for i in range(down-1,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
            dir = (dir+1)%4
        
        return ans
                   
