def part1(days):
    with open("input") as lines:
        a=[]
        line=lines.readline().strip().split(',')
        a=[int(x) for x in line]

    for i in range(0,days):
        k=len(a)
        for j in range(0,k):
            a[j]=a[j]-1
            if(a[j]==-1):
                a.append(8)
                a[j]=6

    return len(a)

print(part1(80))