'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
cache1 = {}

MOD = 10 ** 9 + 9
def answer(n):
    if n < 50000000:
        if n in cache1:
            return cache1[n]
        
        if n == 0:
            cache1[n] = 1
            return cache1[n]
        if n == 1:
            cache1[n] = 10
            return cache1[n]
        
        x = answer(n//2)
        y = answer(n//2 - 1)

        if n % 2 == 0:
            cache1[n] = ( x*x - y*y) % MOD
        else:
            z = answer(n//2 + 1)
            cache1[n] = (x * (z-y)) % MOD
        
        return cache1[n]

    else:
        if n in cache2:
            return cache2[n]
        
        t1 = answer(n//2)
        t2 = answer(n//2 - 1)

        if n % 2 == 0:
            cache2[n] = ( t1*t1 - t2*t2) % MOD
        else:
            t3 = answer(n//2 + 1)
            cache2[n] = (t1 * (t3-t2)) % MOD
        
        return cache2[n]



for _ in range(int(input())):
    n = int(input())
    cache2 = {}
    print(answer(n))
