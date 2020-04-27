score=[100,90,90,80,75,60]
alice=[50,65,77,90,102]
new_set=[]
ans=[]
def binsearch(myscore,scores,start,end):
    middle=(end+start)//2
    if start==end:
        if myscore>=scores[start]:
            myrank[0]=ranks[start]
            return
        else:
            myrank[0]=ranks[start]+1
            return

    if myscore>scores[middle]:
        binsearch(myscore,scores,start,middle-1)
    elif myscore<scores[middle]:
        binsearch(myscore,scores,middle+1,end)
    else:
        myrank[0]=ranks[middle]
        return

temp=score.copy()
for i in alice:      
    
    temp.append(i)
     
    new_set=list(set(temp))
    new_set.sort()
    count=len(new_set)-new_set.index(i)
    ans.append(count)

print(ans)
            
            
            
            
              
