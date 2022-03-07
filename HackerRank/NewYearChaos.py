def minimumBribes(q):
    # Write your code here
    bribes = 0
    n = len(q) - 1
    i = n
    while i >= 0:
        if (q[i]!=i+1):
            if (i-1 >= 0) and (q[i-1] == i+1):
                bribes+=1
                q[i-1],q[i] = q[i],q[i-1]
            elif(i-2)>=0 and (q[i-2] == i+1):
                bribes+=2
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = i+1
                
            else:
                print("Too chaotic")
                return
        i-=1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
