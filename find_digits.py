def findDigits(n):
    a=str(n)
    count=0
    for i in a:
        if(int(i) !=0):
            if(n%int(i)==0):
                count=count+1
    return count
        

t = int(input())
for t_itr in range(t):
        n = int(input())
        result = findDigits(n)
        print(result)
