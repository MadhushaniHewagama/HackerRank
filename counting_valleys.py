s='UDDDUDUU'
ans=0
t=0
for i in s:
    if(i=='D'):
        t=t-1
    else:
        t=t+1
    if(t==0 and i=='U'):
        ans=ans+1
print(ans)
