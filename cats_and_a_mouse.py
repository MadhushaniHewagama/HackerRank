x=22
y=75
z=70
ans=''
if(x>y):
    if(z>=x):
        ans='Cat A'
    elif(z<=y):
        ans='Cat B'
    else:
        if((x-z)>(z-y)):
            ans='Cat B'            
        elif((x-z)<(z-y)):
            ans='Cat A'
        else:
            ans='Mouse C'       
      
elif(x<y):
    if(z<=x):
        ans='Cat A'
    elif(z>=y):
        ans='Cat B'
    else:
        if((y-z)>(z-x)):
            ans='Cat A'            
        elif((y-z)<(z-x)):
            ans='Cat B'
        else:
            ans='Mouse C'      
    
else:
    ans='Mouse C'
  
print(ans)
