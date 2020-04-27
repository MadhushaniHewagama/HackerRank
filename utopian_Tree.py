def utopianTree(n):
    val=1
    for i in range(1,n+1):
        if(val%2==0):
            val=val+1
        else:
            val=val*2
                   
    return(val)   

t = int(input())
for t_itr in range(t):
    n = int(input())
    print(utopianTree(n))
