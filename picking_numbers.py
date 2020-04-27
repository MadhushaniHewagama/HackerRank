a=list(map(int,('7 12 13 19 17 7 3 18 9 18 13 12 3 13 7 9 18 9 18 9 13 18 13 13 18 18 17 17 13 3 12 13 19 17 19 12 18 13 7 3 3 12 7 13 7 3 17 9 13 13 13 12 18 18 9 7 19 17 13 18 19 9 18 18 18 19 17 7 12 3 13 19 12 3 9 17 13 19 12 18 13 18 18 18 17 13 3 18 19 7 12 9 18 3 13 13 9 7').split()))
a.sort()
count=1
ans=1
list_val=[a[0]]

for i in range(1,len(a)):
    if((a[i]-a[i-1])<=1):
        
        print(len(set(list_val)))
        temp=list_val.copy()
        temp.append(a[i])
        if(len(set(temp))<=2):
            count=count+1
            list_val.append(a[i])                
        else:
            count=1
            list_val=[]
            list_val.append(a[i])
                
    else:
        count=1
        list_val=[]
        list_val.append(a[i])
    print(list_val)
    if(ans<count):
        ans=count
print(ans)
