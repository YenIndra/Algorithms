for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    prev = arr[0] ^ arr[1]
    for i in range(1,n-1):
        tmp = arr[i] ^ arr[i+1]
        if tmp < prev:
            prev = tmp
    
    print(prev)
