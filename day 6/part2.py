def part2(days):
    with open("input") as lines:
        a=[]
        line=lines.readline().strip().split(',')
        a=[int(x) for x in line]

    a.sort()
    k=max(a)
    if(k<8):
        k=8

    b=[0]*(k+1)
    for i in range(0,k+1):
        b[i]=a.count(i)

    print(b)
    for i in range(days):
        l=b[0]
        b=b[1:]
        b[6]=b[6]+l
        b.append(l)

    return(sum(b))

print(part2(256))