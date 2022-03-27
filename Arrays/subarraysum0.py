def subArrayExists(self,arr,n):
        #from collections import defaultdict
        ##Your code here
        #Return true or false
        if 0 in arr:
            return True
        else:
            prefix = 0
            hash = {0:1}
            for i in arr:
                prefix+=i
                if prefix in hash:
                    return True
                hash[prefix] = 1
            return False
