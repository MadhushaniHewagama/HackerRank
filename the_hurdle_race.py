def hurdleRace(k, height):
    ans=0
    max_val=0
    for i in height:
        if(k<i):
            ans=i-k
            if(ans>max_val):
                max_val=ans
    return max_val


nk = input().split()
n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))
result = hurdleRace(k, height)
print(result)
