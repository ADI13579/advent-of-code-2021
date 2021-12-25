def part1():
    a=[]
    with open("input") as lines:
        for line in lines:
            a.append("9"+line.strip()+"9")
    x=len(a[0])
    a.append("9"*x)
    a.insert(0, "9"*x)
    y=len(a)

    sum=0
    for i in range(1,y-1):
        for j in range(1,x-1):
            if(a[i][j]<a[i-1][j]):
                if(a[i][j]<a[i+1][j]):
                    if(a[i][j]<a[i][j-1]):
                        if(a[i][j]<a[i][j+1]):
                            sum=sum+int(a[i][j])+1
    return sum
                
                

print(part1())