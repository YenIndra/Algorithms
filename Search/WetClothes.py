'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n,m,g = list(map(int,input().split()))
time = list(map(int,input().split()))
clothes = list(map(int,input().split()))

count  = 0
prev = time[0]
went_out = False
went_out_count = 0
diffarr = []
for i in range(1,n):
    diff = time[i] - prev
    diffarr.append(diff)
    prev = time[i]
diffarr.sort(reverse = True)
#print(diffarr)
j_count = 0
j = 0
k = 0
while k < (g):
    while j < len(clothes):
        if clothes[j] <= diffarr[k]:
            count+=1
            went_out = True
            clothes.pop(j)
        else:
            j+=1
    #print(clothes)
    if went_out == True:
        k+=1
    if len(clothes) == m:
        break

print(count)
exit()



for i in range(1,n):
    if went_out_count > g:
        break
    diff = time[i] - prev
    print(diff)
    j = 0
    while j < len(clothes):
        if clothes[j] <= diff:
            count+=1
            went_out = True
            clothes.pop(j)
            #print(clothes)
        else:
            j+=1
    if went_out == True:
        went_out_count+=1
    prev = time[i]
print(count)
    

