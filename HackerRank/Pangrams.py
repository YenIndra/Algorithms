def pangrams(s):
    # Write your code here
    #s.replace(' ','')
    res = set()
    s = s.lower()
    print(s)
    for i in s:
        if i>='a' and i<='z':
            res.add(i)
    print(res,"   ",len(res))
    if len(res) == 26:
        return 'pangram'
    else:
        return 'not pangram'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
