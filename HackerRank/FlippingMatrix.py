#Sean invented a game involving a  matrix where each cell of the matrix contains an integer. 
#He can reverse any of its rows or columns any number of times. 
#The goal of the game is to maximize the sum of the elements in the  submatrix located in the upper-left quadrant of the matrix.
#Given the initial configurations for  matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the 
#sum of the elements in the matrix's upper-left quadrant is maximal.



def flippingMatrix(matrix):
    # Write your code herer
    n = len(matrix)//2
    sum = 0
    for i in range(n):
        for j in range(n):
            r1 =i
            r2 = 2*n-i-1
            c1 = j
            c2 = 2*n-j-1
            sum+= max(
                max(matrix[r1][c1],matrix[r1][c2]),
                max(matrix[r2][c1],matrix[r2][c2])
            )
    
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
