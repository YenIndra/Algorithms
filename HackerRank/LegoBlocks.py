def legoBlocks(n, m):
    # Write your code here
    M = 10 ** 9 + 7
    f = [1,1,2,4]
    for i in range(4,m+1):
        f.append(sum(f[-4:]))
    F = [0,1]
    for i in range(2,m+1):
        h = f[i] = pow(f[i],n,M)
        for j in range(1,i):
            h -= F[j]*f[i-j]
        F.append(h%M)
    return F[-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
