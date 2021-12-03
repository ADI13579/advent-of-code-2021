def part2():
    position=0
    aim=0
    depth=0
    with open("input",'r') as lines:
        for line in lines:
            line=line.rstrip()
            [x,command]=[int(line[-1:]),line[:-2]]
            if(command=="forward"):
                position=position+x
                depth=depth+aim*x
            elif(command=="up"):
                aim=aim-x
            elif(command=="down"):
                aim=aim+x
    return(depth*position)

print(part2())