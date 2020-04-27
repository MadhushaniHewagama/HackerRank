def beautifulDays(i, j, k):
    count=0
    for i in range(i,j+1):
        val=int(str(i)[::-1])
        if(abs(val-i)%k==0):
            count=count+1
    return count


ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
result = beautifulDays(i, j, k)
print(result)
