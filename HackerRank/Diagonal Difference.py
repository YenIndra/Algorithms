def diagonalDifference(arr):
    # Write your code here
    leftdiag,rightdiag =0,0
    for i in range(len(arr)):
        leftdiag+=arr[i][i]
        rightdiag+=arr[i][-i-1]
    return abs(leftdiag-rightdiag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
