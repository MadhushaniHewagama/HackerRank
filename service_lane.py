def serviceLane(n, cases):
    #print(width)
    ans=[]
    for i in cases:
        ans.append(min(width[i[0]:i[1]+1]))
    return ans


nt = input().split()
n = int(nt[0])
t = int(nt[1])
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

result = serviceLane(n, cases)
print(result)
