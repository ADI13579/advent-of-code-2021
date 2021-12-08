fixed=[2,3,4,7]
count=0
with open("input") as lines:
    for line in lines:
        line=line.split('|')[1].strip()
        line=line.split(" ")
        for i in line:
            if(len(i) in fixed):
                count=count+1

print(count)