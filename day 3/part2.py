def part2():
    a=[[],[]]
    b=[]
    with open("input",'r') as lines:
        for line in lines:
            line=line.rstrip()
            b.append(line)

    length=len(b[0])
    flag=["0"]*length
    
    for i in range(0,length):
        for k in b:
            if(k[i]=="1"):
                a[0].append(k)
            else:
                a[1].append(k)
        
        if(len(a[0])>len(a[1])):
            b=a[0]
        elif(len(a[0])==len(a[1])):
            b=a[0]
        else:    
            b=a[1]
        
        a=[[],[]]

    c=b[0]

    a=[[],[]]
    b=[]    
    
    with open("input",'r') as lines:
        for line in lines:
            line=line.rstrip()
            if(line[0]!=c[0]):
                b.append(line)

    for i in range(1,length):
        for k in b:
            if(k[i]=="0"):
                a[0].append(k)
            else:
                a[1].append(k)
        
        if(len(a[0])==1):
            b=a[0]
            break
        elif(len(a[1])==1):
            b=a[1]
            break
             
        if(len(a[0])<len(a[1])):
            b=a[0]
        elif(len(a[0])==len(a[1])):
            b=a[0]
        else:    
            b=a[1]
        a=[[],[]]

    d=b[0]
    sum=[0,0]
    print(c,d)
    for i in range(0,length):
        if(c[i]=="1"):
            sum[0]=sum[0]+pow(2,length-i-1)
        if(d[i]=="1"):
            sum[1]=sum[1]+pow(2,length-i-1)
            
    return sum[0]*sum[1]

print(part2())