def part2():
    fixed={2:1,3:7,4:4,7:8}
    fixed_keys=fixed.keys()
    print(fixed_keys)
    a={}
    sum=0
    with open("input") as lines:
        for line in lines:
            line=line.replace('|','').strip().split()
            for i in line:
                k=len(i)
                if(k in fixed_keys):
                    a[fixed[k]]=i

            line=line[-4:]
            l=0
            for i in range(4):
                l=l*10
                k=len(line[i])
                signalset=set(line[i])
                if(k==5):
                    if(len(set(a[1])&signalset)==2):
                        l=l+3
                    elif(len(set(a[4])&signalset)==2):
                        l=l+2
                    else:
                        l=l+5
                elif(k==6):
                    if(len(set(a[1])&signalset)==1):
                        l=l+6        
                    elif(len(set(a[4])&signalset)==4):
                        l=l+9
                    else:
                        l=l+0
                else:
                    for key,value in a.items():
                        if(set(value)==signalset):
                            l=l+key
                            break
            sum=sum+l
    return sum

print(part2())