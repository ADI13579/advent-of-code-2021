with open("input") as numbers:
    temp=numbers.readline().strip().split(',')
    num=[int(x) for x in temp]

num.sort()
n=((len(num)+1)/2)
n=n-1

median=num[int(n)]
if(n>int(n)):
    median=int((median+num[int(n)+1])/2)

sum=0
print(median)
for i in num:
    sum=abs(i-median)+sum

print(sum)