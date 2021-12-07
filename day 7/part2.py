with open("input") as line:
    temp=line.readline().strip().split(',')

num=[int(x) for x in temp]

mean=(sum(num)/len(num)).__round__()
num.sort()

last=num[len(num)-1]
fuel=[0]

for i in range(1,last-mean+1):
    fuel.append(fuel[i-1]+i)

sum=0
for j in num:
    sum=sum+fuel[abs(j-mean)]

print(sum)
