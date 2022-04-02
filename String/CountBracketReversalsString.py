def countRev (s):
    # your code here
    
    stack = []
    n = len(s)
    ans=0
    if n%2:
        return -1
    
    for bracket in s:
        if bracket == '{':
            stack.append(bracket)
            
        else:   
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append('{')
                ans+=1
            
    if len(stack) % 2 == 0:
        ans+=len(stack)//2
    else:
        return -1
      
    return ans
