def cookies(k, A):
    # Write your code here
    import heapq
    heapq.heapify(A)
    count = 0
    while (A[0] < k) and len(A) > 1:
        count+=1
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        final = (first + (2*second))
        heapq.heappush(A,final)
    if len(A) > 1:
        return count
    else:
        if A[0] >=k:
            return count
        else:
            return -1
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
