def getPairsCount(self, arr, n, k):
        # code here
        freqmap = {}
        count = 0
        for i in arr:
            diff = k - i
            if diff in freqmap:
                count+=freqmap[diff]
            if i in freqmap:
                freqmap[i]+=1
            else:
                freqmap[i] = 1
        return count
