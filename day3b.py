filename = "day3.txt"
lines = open(filename,'r').read().splitlines()
matrix = [[0 for i in range(1000)] for i in range(1000)]

def readLine(line):
    import re
    result = re.split('#| @ |,|: |x',line)
    return result[1:]

def addArea(matrix,claimid,xstart,ystart,xsize,ysize):

    for x in range(xstart,(xstart+xsize)):
        for y in range(ystart,(ystart+ysize)):
            if matrix[x][y] == 0:
                matrix[x][y] = claimid
            else:
                matrix[x][y] = "X"
    return matrix

def checkArea(matrix,claimid,xstart,ystart,xsize,ysize):
    for x in range(xstart,(xstart+xsize)):
        for y in range(ystart,(ystart+ysize)):
            if matrix[x][y] == "X":
                return False
    return claimid
    



      
for line in lines:
    overlap = 0
    result = readLine(line)
    claimid = int(result[0])
    xstart = int(result[1])
    ystart = int(result[2])
    xsize = int(result[3])
    ysize = int(result[4])
    matrix = addArea(matrix,claimid,xstart,ystart,xsize,ysize)
    print("Added claim Id:",claimid)
#print(sum(item.count("X") for item in matrix)) 

for line in lines:
    result = readLine(line)
    claimid = int(result[0])
    xstart = int(result[1])
    ystart = int(result[2])
    xsize = int(result[3])
    ysize = int(result[4])
    response = checkArea(matrix,claimid,xstart,ystart,xsize,ysize)
    if response != False:
        print("claimid not overlapped ",response)






