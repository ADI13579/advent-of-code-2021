def part1():
    with open("input",'r') as lines:
        linecount=0
        k=len(lines.readline().rstrip())
        lines.seek(0)
        a=[0]*k
        for line in lines:
            line=line.rstrip()
            linecount=linecount+1
            for i in range(0,k):
                if(line[i]=="1"):
                    a[i]=a[i]+1

    gamma=0
    epsilon=0
    for i in range(0,k):
        if(linecount/2<a[i]):
            gamma=gamma+pow(2,k-i-1)
        else:
            epsilon=epsilon+pow(2,k-i-1)

    return gamma*epsilon

print(part1())