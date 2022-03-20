from collections import Counter
for _ in range(int(input())):
    n = int(input())
    heights = list(map(int,input().split()))
    heights_count = Counter(heights)
    ls = []
    for i in heights_count:
        ls.append(heights_count[i])
    ls.sort()
    diff = -1
    x = len(ls)
    for j in range(x-1,0,-1):
        if (ls[j] - ls[0]) > diff:
            diff = ls[j] - ls[0]

    print( diff )
