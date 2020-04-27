keyboards=[3,1]
drives=[5,2,8]
b=10
ans=''
max_cost=0
for i in keyboards:
    for j in drives:
        if(i+j<=b):
            if(max_cost<(i+j)):
                max_cost=i+j
if(max_cost !=0):
    ans=str(max_cost)
else:
    ans='-1'
print(ans)
