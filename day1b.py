filename = "day1.txt"
lines = open(filename,'r').read().splitlines()
total = 0
totalList = []
found = False
while not found:
    print(".",end="")

    for num in lines:
        total += int(num)
        if total in totalList:
            found = True
            print(total)
            break
        else:
            totalList.append(total)
            
print("end")
print(total)




