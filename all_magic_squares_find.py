import itertools
a_list=[1,2,3,4,5,6,7,8,9]
all_combinations=itertools.permutations(a_list)

def magic_square(m):
    r1=m[0]+m[1]+m[2]
    r2=m[3]+m[4]+m[5]
    r3=m[6]+m[7]+m[8]
    c1=m[0]+m[3]+m[6]
    c2=m[1]+m[4]+m[7]
    c3=m[2]+m[5]+m[8]
    d1=m[0]+m[4]+m[8]
    d2=m[2]+m[4]+m[6]
    if(r1==r2 and r2==r3 and r3==c1 and c1==c2 and c2==c3 and c3==d1 and d1==d2):
        return True
    else:
        return False
    
    
for i in all_combinations:
    
    if(magic_square(i)):
        matrix=[]
        row=[]
        c=0
        for j in i:
            c=c+1
            row.append(j)
            if(c%3==0):
                matrix.append(row)
                row=[]
                
        print(matrix)
           
            
    
        
