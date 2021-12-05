from part1 import board

def part2():
    with open("input") as lines:
        line=lines.readline().strip()
        numbers=line.split(',')
        b=[]
        c=[]
        d=[]
        for line in lines:
            a=line.strip().split()
            if(len(a)==5):
                b.append(a)
            if(len(b)==5):
                c.append(board(b))
                b=[]

    for i in numbers:
        for j in c:
            j.remove(i)
            if(not j.check()):
                d.append(j)
           
        if(len(d)==0):
            return j
        c=d
        d=[]

sum=0
ans=part2()
ans.print()
for i in ans.numbers:
    for j in i:
        if(j!=" "):
            sum=sum+int(j)
print(sum*int(ans.last))