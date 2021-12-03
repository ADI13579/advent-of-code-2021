def part1():
    depth=0
    position=0
    with open("input",'r') as lines:
        for line in lines:
            line=line.rstrip()
            [x,command]=[int(line[-1:]),line[:-2]]
            if(command=="forward"):
                position=position+x
            elif(command=="up"):
                depth=depth-x
            elif(command=="down"):
                depth=depth+x
    return(depth*position)

print(part1())