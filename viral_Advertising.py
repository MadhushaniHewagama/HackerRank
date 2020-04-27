
def viralAdvertising(n):
    cumulative=0
    shared=5
    like=2
    for i in range(1,n+1):
        like=int(shared/2)
        cumulative=cumulative+like
        shared=int(shared/2)*3
        
    return cumulative
        

n = int(input())
result = viralAdvertising(n)
print(result)
