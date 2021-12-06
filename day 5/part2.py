n=1000
c=[[0]*n for x in range(n)]

def part2():
    with open("input") as lines:
        a=[]
        count=0
        for line in lines:
            line=line.strip().replace(' -> ',',').split(',')
            a=[int(x) for x in line]
            print(a)
            if(a[0]==a[2]):
                if(a[1]>a[3]):
                    a[1],a[3]=a[3],a[1]
                for j in range(a[1],a[3]+1):
                      c[j][a[0]]=c[j][a[0]]+1
            else:
                m=(a[1]-a[3])/(a[0]-a[2])
                if(a[0]>a[2]):          
                    a[0],a[2]=a[2],a[0]
                    a[1],a[3]=a[3],a[1]
                for j in range(a[0],a[2]+1):
                    y=int(m*(j-a[0])+a[1])
                    c[y][j]=c[y][j]+1

    count=0
    for i in c:
        for j in i:
            if(j>1):
                count=count+1
    
    return count              
    
print(part2())