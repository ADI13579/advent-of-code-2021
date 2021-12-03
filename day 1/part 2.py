def part2():
    with open("input",'r') as lines:
        a=[]
        while(len(a)<3 and lines):
            a.append(int(lines.readline().rstrip()))
            print(a)
        #if there are no three elements in a then error nedded to be thrown here
        increased=0
        b=sum(a)
        for line in lines:
            a.append(int(line.rstrip()))
            a=a[1:]
            c=sum(a)
            if(c>b):
                increased=increased+1
            b=c
    return increased

print(part2())