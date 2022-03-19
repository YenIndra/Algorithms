for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    m = ''
    p = -1
    d = None
    for i in range(n):
        if m < s:
            m = s
            d = i
        elif m == s:
            p = i-d
            break
        s = s[1:]+s[:1]
    if p == -1:
        print(d + (k-1) * n)
    else:
        print(d + (k-1) * p)
