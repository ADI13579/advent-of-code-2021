def part1():
    with open("input") as lines:
        b=[]
        a=[]
        ymin=xmin=float('inf')
        xmax=ymax=float('-inf')
        count=0
        for line in lines:
            count=count+1
            line=line.strip().replace(' -> ',',').split(',')
            if(line[0]==line[2] or line[1]==line[3]):
                a=[int(x) for x in line]
                if(a[0]>a[2]):
                    a[0],a[2]=a[2],a[0]
                elif(a[1]>a[3]):
                    [a[1],a[3]]=[a[3],a[1]]
                xmax=max(xmax,a[2])
                ymax=max(ymax,a[3])
                b.append(a)

        c=[[0 for i in range(xmax+1)] for j in range(ymax+1)]

        for i in b:
            if(i[0]==i[2]):
                for j in range(i[1],i[3]+1):
                    c[j][i[0]]=c[j][i[0]]+1
            else:
                for j in range(i[0],i[2]+1):
                    c[i[1]][j]=c[i[1]][j]+1

        count=0
        for i in c:
            for j in i:
                if(j>1):
                    count=count+1
        
        return count

print(part1())