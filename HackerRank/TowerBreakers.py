def towerBreakers(n, m):
    # Write your code here
    tower = [m]*n
    counter = 1
    turn = 1
    for i in range(n):
        if tower[i] == 1:
            continue
        else:
            tower[i] = 1
            counter+=1
            turn = counter%2
    if turn == 1:
        return 2
    else:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
