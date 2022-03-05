def solve(str_arr):
    new_str = ""
    n = len(str_arr)
    new_str = str_arr[0]
    c = 0
    for i in range(1,n):
        if str_arr[i] != new_str[c]:
            new_str += str_arr[i]
            c+=1
    
    return new_str


for _ in range(int(input())):
    a = input()
    print(solve(a))
