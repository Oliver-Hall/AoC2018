filename = "day5.txt"
polymer = open(filename,'r').read()
print(polymer)

def compareTwo(polymer,inum):

    try:       
        first = polymer[inum]
        second = polymer[inum+1]
    except:
        print(polymer)
        print()
        print(len(polymer))
        quit()
    if first.lower() == second.lower() and ((first.isupper() and second.islower()) or (first.islower() and second.isupper())):
        newPolymer = polymer[:inum] + polymer[(inum+2):]
        removed = True
    else:
        newPolymer = polymer
        removed = False
    #print("index:",inum)
    print("newPolymer length:",len(newPolymer),end='\r')
    return newPolymer,removed

def shrinkPolymer(polymer):
    i = 0
    while i<=(len(polymer)-2):
        polymer,removed = compareTwo(polymer,i)
        if removed == False:
            i += 1
        else:
            if i > 3:
                i-= 3
            else:
                i = 0
    print()
    print("Final Length",len(polymer))
    print()

def findSymbols(polymer):
    symList = []
    for sym in polymer:
        if sym.lower() not in symList:
            symList.append(sym.lower())
    print(symList)
    
    
shrinkPolymer(polymer)







# def checkPolymer(polymer,start):
#     print("started again")
#     removed = False
#     while (start < len(polymer)):
#         print("index",start)
#         polymer,removed = compareTwo(polymer,start)
#         if removed:
#             start = 0
#             checkPolymer(polymer,start)
#         else:
#             start += 1
#             checkPolymer(polymer,start)
# checkPolymer(polymer,0)


