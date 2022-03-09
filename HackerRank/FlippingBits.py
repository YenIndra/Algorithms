def flippingBits(n):
    # Write your code here
    binary_num = bin(n).replace('0b','')
    n = len(binary_num)
    if(n<32):
        left = 32-n
        temp = '0' * left
        binary_num = temp + binary_num
        
    print(binary_num)
    new_bin = ''
    for i in range(len(binary_num)):
        if binary_num[i] == '0':
            new_bin+='1'
        else:
            new_bin+='0'
    print(new_bin)
    deci = int(new_bin,2)
    return(deci)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
