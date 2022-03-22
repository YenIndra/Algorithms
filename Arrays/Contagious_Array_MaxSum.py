def maxSubArraySum(self,arr,N):
        ##Your code here
        currsum = 0
        sum1 = -100000000
        for i in range(0,N):
            currsum += arr[i]
            
            if currsum > sum1 :
                sum1 = currsum
            if currsum < 0:
                currsum = 0
        return sum1
