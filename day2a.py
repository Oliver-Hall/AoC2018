filename = "day2.txt"
codes = open(filename,'r').read().splitlines()
#print(codes)
alpha = "abcdefghijklmnopqrstuvwxyz"
numtwos = 0
numthrees = 0

for item in codes:
    sort = ''.join(sorted(item))
    print(sort)
    twoletters = False
    threeletters = False
    counts = { letter: item.count(letter) for letter in alpha }
    print(counts)
    for key , value in counts.items():
        if value == 2:
            twoletters = True
        elif value == 3:
            threeletters = True
    
    if twoletters:
        numtwos+=1
    if threeletters:
        numthrees+=1
    print(numtwos,numthrees)

final = numtwos * numthrees
print(final)

