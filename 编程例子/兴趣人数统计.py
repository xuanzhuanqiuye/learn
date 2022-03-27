
count={}

with open("./students.txt",encoding="utf-8") as fin:
    for line in fin:
        line=line[:-1]
        name,likes=line.split(" ")
        like=likes.split(",")
        for l in like:
            if l not in count:
                count[l]=0
            count[l]+=1

print(count)