def jumpingOnClouds(c):
    val=0
    jump=0
    while(True):
        if(val>=(len(c)-1)):
            break
        if(c[val] ==0):
            val=val+2
            jump=jump+1
        else:
            val=val-1        
    return (jump)
        
            
        

nk = input().split()
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)
print(result)
# c[(i+k)%n]
