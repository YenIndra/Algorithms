s,n = input().split()
n = int(n)

ls = []
for i in range(len(s)):
    ls.append(s[i:])
ls.sort()
print(ls[n-1])
