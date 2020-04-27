def permutationEquation(p):
    p_list=p
    ans=[]
    for i in range(1,len(p_list)+1):
        val=p_list.index(i)+1
        ans.append(p_list.index(val)+1)
        
    return ans

n = int(input())
p = list(map(int, input().rstrip().split()))
result = permutationEquation(p)
print(result)

#p(p(y))=x
