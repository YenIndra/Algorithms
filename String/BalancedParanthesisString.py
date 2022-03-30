def ispar(self,x):
        # code here
        if len(s) % 2 != 0:
            return False
  
        stack = []
        closing = ['}', ']', ')']
        pairs = {'}':'{', ']':'[', ')':'('}
  
        for bracket in s:
            if bracket in closing:
                if not stack or stack.pop() != pairs.get(bracket):
                    return False
            else:   
                stack.append(bracket)
      
        return True if not stack else False
