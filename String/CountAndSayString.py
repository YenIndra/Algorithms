cache = {}
class Solution:
    
    def countAndSay(self, n: int) -> str:
        if n<=1:
            return "1"
        prev = n-1
        #print(prev)
        if prev not in cache:
            cache[prev] = self.countAndSay(prev)
        
        prevsay = cache[prev]
        j,l = 0,len(prevsay)
        temp = ""
        count = 1
        while j < l:
            a = prevsay[j]
            while(j+1) < l:
                if prevsay[j] == prevsay[j+1]:
                    count+=1
                    j+=1
                else:
                    break
                
            j+=1
            temp+=str(count)+a
            count = 1
        cache[n] = temp
        #print(cache)
        return cache[n]
            
        
