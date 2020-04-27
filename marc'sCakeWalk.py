import itertools
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    print(calorie)
    c=0
    ans=0
    for i in calorie:
        ans=ans+i*(2**c)
        c=c+1
    return ans
            

n = int(input())

calorie = list(map(int, input().rstrip().split()))

result = marcsCakewalk(calorie)
print(result)
