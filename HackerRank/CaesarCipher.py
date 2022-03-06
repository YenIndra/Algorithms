def caesarCipher(s, k):
    # Write your code here
    new_str = ''
    for ch in s:
        if ('A' <= ch <= 'Z'):
            val = (ord(ch)+k-ord('A'))%26
            new_str+=chr(val+ord('A'))
        elif ('a' <= ch <= 'z'):
            val = (ord(ch)+k-ord('a'))%26
            new_str+=chr(val+ord('a'))
        else:
            new_str+=ch
    
    return new_str
                
                
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
