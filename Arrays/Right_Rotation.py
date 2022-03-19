for _ in range(int(input())):
    N,K = input().split(' ') 
    arr = input().split(' ')
    n = int(N)
    k = int(K)
    k = k%n
    newk = n - k
    arr = arr[newk:] + arr[:newk]
    for i in range(n):
        if i == n-1:
            print(arr[i])
        else:
            print(arr[i],end = ' ')
