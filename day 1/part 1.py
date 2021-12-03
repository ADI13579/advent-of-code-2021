def part1():
    increased=0
    with open("input",'r') as lines:
        a=int(lines.readline().rstrip())
        for line in lines:
            b=int(line.rstrip())
            if(b>a):
                increased=increased+1
            a=b
    return increased

print(part1())