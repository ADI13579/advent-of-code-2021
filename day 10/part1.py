with open("input") as lines:
    open=['(','[','<','{']
    close=[')',']','>','}']
    points=[3,57,1197,25137]
    ans=0
    for line in lines:
        s=[]
        sum=0
        line=line.strip()
        for i in line:
            if(i in open):
                s.append(i)
            else:
                k=close.index(i)
                print(k)
                p=s.pop()
                if(p!=open[k]):
                    sum=sum+points[k]
            print(s)
            input()
            
print(ans)