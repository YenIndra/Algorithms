from bisect import bisect_left

n = int(input())
alpha = []
for i in range(n):
    alpha.append(input())

sortedlist = []
for i in range(1,n+1):
    idx = bisect_left(sortedlist,alpha[i-1])
    print(idx)
    sortedlist.insert(idx,alpha[i-1])

###################OR##################################

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
    count = 0
    for j in range(i):
        if arr[j] < arr[i]:
            count+=1
    
    print(count)
