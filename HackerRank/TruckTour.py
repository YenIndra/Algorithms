def truckTour(petrolpumps):
    # Write your code here
    avail,total_avail,start = 0,0,0
    for i in range(len(petrolpumps)):
        gas,cost = petrolpumps[i]
        total_avail+= gas - cost
        avail += gas - cost 
        if avail < 0:
            avail = 0
            start = i+1
    
    return -1 if (total_avail < 0) else start
    print(petrolpumps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
