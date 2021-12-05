class board:
    def __init__(self,c):
        self.numbers=c
        self.last=0
        self.moves=0

    def print(self):
        for i in self.numbers:
            print(i)
        print("\n")
    
    def remove(self,x):
        for i in range(0,5):
            for j in range(0,5):
                if(self.numbers[i][j]==x):
                    self.numbers[i][j]=" "
                    self.last=x
                    self.moves=self.moves+1
                    return 1
        return 0
    
    def check(self):
        if(self.moves<5):
            return 0
        else:
            for i in range(0,5):
                if(self.numbers[i][i]==" "):
                    a=[1,1]
                    for j in range(0,5):
                        a[0]=a[0] and (self.numbers[i][j]==" ")
                        a[1]=a[1] and (self.numbers[j][i]==" ")
                    if(a[0] or a[1]):
                        return 1
        return 0    


def part1():
    with open("input") as lines:
        line=lines.readline().strip()
        numbers=line.split(',')
        b=[]
        c=[]
        for line in lines:
            a=line.strip().split()
            if(len(a)==5):
                b.append(a)
            if(len(b)==5):
                c.append(board(b))
                b=[]

    for i in numbers:
             for j in range(0,len(c)):
                 if(c[j].remove(i)):
                     if(c[j].check()):
                         return c[j]

sum=0
ans=part1()
ans.print()
for i in ans.numbers:
    for j in i:
        if(j!=" "):
            sum=sum+int(j)

print(sum*int(ans.last)) 