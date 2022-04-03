def longestCommonPrefix(self, strs: List[str]) -> str:
        
        l = 201
        for s in strs:
            l = min(l,len(s))
        i = 0
        while i < l:
            st = set([s[0:i+1] for s in strs])
            print(st)
            if (len(st) == 1 and st != {''}):
                i+=1
            elif len(st) > 1:
                print('Ran2')
                return strs[0][0:i]
            elif st == {''}:
                return ''
        return strs[0][0:l]
