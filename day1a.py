filename = "day1a.txt"
lines = open(filename,'r').read().splitlines()
print(lines)
total = 0
for num in lines:
    total += int(num)
print(total)



