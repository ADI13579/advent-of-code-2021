def part1():
    with open("input") as numbers:
        temp=numbers.readline().strip().split(',')
        num=[int(x) for x in temp]

    num.sort()
    n=((len(num)+1)/2)-1
    median=num[int(n)]
    if(n>int(n)):
        median=int((median+num[int(n)+1])/2)

    fuel=0
    print(median)
    for i in num:
        fuel=abs(i-median)+fuel
    return fuel

print(part1())