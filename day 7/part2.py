def part2():
    with open("input") as line:
        temp=line.readline().strip().split(',')

    num=[int(x) for x in temp].sort()
    num.sort()
    fuelconst=[0]

    mean=int(sum(num)/len(num).__round__())
    
    k=last_num=num[-1:][0]+1
    for i in range(1,k):
        fuelconst.append(fuelconst[i-1]+i)

    fuel=0
    for j in num:
        fuel=fuel+fuelconst[abs(j-mean)]

    return fuel

print(part2())