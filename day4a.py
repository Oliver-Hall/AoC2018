import re
import time
from datetime import datetime
from dateutil.parser import parse
from time import strptime

filename = "day4sorted.txt"
lines = open(filename,'r').read().splitlines()


t_fmt = '%Y-%m-%d %H:%M' # format of time stamps
t_pat = re.compile(r'\[(.*?)\]') # pattern to extract timestamp
for l in sorted(lines, key=lambda l: strptime(t_pat.search(l).group(1), t_fmt)):
    sorted_times.append(l)

#print(sorted_times)
def writeSortedFile():
    with open('day4sorted.txt', 'w') as f:
        for item in sorted_times:
            f.write("%s\n" % item)


# writeSortedFile()

# def calcGuardSleepTimes(sorted_times):
#     #Guard #811 begins shift
#     guardDict = {}
#     currentGuard = 0
#     for line in sorted_times:
#         matchguard = re.search(r'#\d+', line)
#         if matchguard:
#             currentGuard = matchguard.group()[1:]
#             if currentGuard not in guardDict:
#                 guardDict[currentGuard] = 0

#         else:
#             matchshift = re.search(r'falls asleep',line)

#             guardDict[currentGuard] += 1

#     print(guardDict)


guardDict = {}
currentGuard = 0
starttime = 0
endtime = 0 
highestMinDict ={}


for line in lines:
    numbers = re.findall(r'\d+', line)
    if len(numbers) == 6:
        #new guard
        currentGuard = numbers[5]
        print("New guard",currentGuard)

        if currentGuard not in guardDict:
            guardDict[currentGuard] = 0
            highestMinDict[currentGuard] = {}
            for eachmin in range(0,60):
                highestMinDict[eachmin] = 0

        
    else:
        if line[19:20] == 'f':
            # falls asleep
            print("Guard {} falls asleep".format(currentGuard))
            starttime = int(numbers[4])
        elif line[19:20] == 'w':
            # wakes up
            endtime = int(numbers[4])
            for x in range(starttime,endtime+1):
                highestMinDict[x] += 1
                #print(highestMinDict)
            asleep = endtime-starttime

            
            guardDict[currentGuard] += asleep
            print("Guard {} wakes up - now at {} minutes".format(currentGuard,guardDict[currentGuard]))

highestGuard = max(guardDict, key=guardDict.get)
print("Highest Guard",highestGuard)
print("Minutes asleep for this guard: ",highestMinDict)
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
highestmin = keywithmaxval(highestMinDict)
print("highest minute asleep",highestmin)

final = int(highestGuard)*highestmin
print("final",final)




       


             

#calcGuardSleepTimes(lines)