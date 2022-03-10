#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    costhash = {}
    for i in range(len(cost)):
        comp = money - cost[i]
        if comp in costhash:
            print(costhash[comp],i+1)
            return
        else:
            costhash[cost[i]] = i+1

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
