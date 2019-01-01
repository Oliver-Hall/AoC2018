filename = "day2.txt"
codes = open(filename,'r').read().splitlines()
numcodes = len(codes)
second = 1

for first in range(numcodes):
    for second in range(first+1,numcodes):
        s1 = codes[first]
        s2 = codes[second]

        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diff) == 1:
            print(s1,s2)
            finalcommon = []
            for x in range(len(s1)):
                if s1[x] == s2[x]:
                    finalcommon.append(s1[x])
            print(finalcommon)
            final = ''.join(finalcommon)
            print(final)
