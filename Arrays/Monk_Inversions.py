for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        temp =  input().split()
        temp = [int(i) for i in temp]
        arr.append(temp)
    count = 0
    for i in range(n):
        for j in range(n):
            for x in range(i,n):
                for y in range(j,n):
                    if arr[i][j] > arr[x][y]:
                        count+=1

    print(count)
