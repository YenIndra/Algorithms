def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    i = 0
    j = len(s)-1
    while i < len(s)//2:
        if(s[i] != s[j]):
            break
        i+=1
        j-=1
    if i > j:
        return -1
    
    a = i+1
    b = j
    while(a<j):
        if(s[a]!=s[b]):
            return j
        a+=1
        b-=1
    return i
    
