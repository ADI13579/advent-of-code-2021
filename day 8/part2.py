def part2():
    #stored as 1,7,4,8
    fixed=[2,3,4,7]
    string=[""]*4
    k=[0]*4
    sum=0
    with open("input") as lines:
        for line in lines:
            line=line.strip().split()
            line.remove('|')
            for i in line:
                k=len(i)
                for j in range(0,4):
                    if(k==fixed[j]):
                        string[j]=i
                        break
            a={'1':string[0],'7':string[1],'4':string[2],'8':string[3]}
            # As this passes every input has atleast the digits 1,4,7,8
            # for i in string:
            #     if(i==""):
            #         print("error")
            line=line[-4:]
            l=0
            for i in range(4):
                l=l*10
                k=len(line[i])
                if(k==5):
                    if(len(set(a['1'])&set(line[i]))==2):
                        l=l+3
                    elif(len(set(a['4'])&set(line[i]))==2):
                        l=l+2
                    else:
                        l=l+5
                elif(k==6):
                    if(len(set(a['1'])&set(line[i]))==1):
                        l=l+6        
                    elif(len(set(a['4'])&set(line[i]))==4):
                        l=l+9
                    else:
                        l=l+0
                elif(k==fixed[0]):
                    l=l+1
                elif(k==fixed[1]):
                    l=l+7
                elif(k==fixed[2]):
                    l=l+4
                elif(k==fixed[3]):
                    l=l+8
            sum=sum+l
    return sum

print(part2())