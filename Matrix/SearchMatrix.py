def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #ans = False
        col = len(matrix[0]) - 1
        row = 0
        
        while row<=len(matrix)-1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col-=1
            else:
                row+=1
            
                
        return False
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #ans = False
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1 # 2D to 1D
        
        while start <= end:
            mid = start + (end - start) // 2
            # 1D to 2D
            mid_val = matrix[mid//cols][mid%cols]
            
            if target == mid_val:
                return True
            elif target < mid_val:
                end = mid - 1 
            else:
                start = mid+1
        
        return False
        
