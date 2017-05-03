import csv
import sys

def readcsv(fname):
    f = open(fname, 'r')
    reader = csv.reader(f)
    lines = list(reader)
    f.close()
    return lines

def writecsv(data):
    f = open('test.csv', "wb")
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for line in data:
        writer.writerow(line)

filename = "inputData/Batting.csv"
unfiltered = readcsv(filename)[1:]
yearFilter = []
testFilter = []
iterator = 0
minYear = 1956
maxYear = 2016
testPass = True

for line in unfiltered:
    if int(line[1]) >= minYear and int(line[1]) <= maxYear:
        yearFilter.append(line)

yearFilter.sort()

if "no-stints" in sys.argv:
    while iterator < len(yearFilter):
        if(yearFilter[iterator][2] != "1"):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1
    iterator = 0
    while iterator < len(yearFilter):
        if(yearFilter[iterator][2] != "1"):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

else:
    iterator = len(yearFilter) - 1
    while iterator > 0:
        if(yearFilter[iterator][2] != "1"):
            subiterator = 5
            while subiterator < 22:
                yearFilter[iterator - 1][subiterator] = str(int(yearFilter[iterator - 1][subiterator]) + int(yearFilter[iterator][subiterator]))
                subiterator = subiterator + 1
        iterator = iterator - 1
    iterator = 0
    while iterator < len(yearFilter):
        if(yearFilter[iterator][2] != "1"):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "g-max" in sys.argv:
    maxG = sys.argv[sys.argv.index("g-max") + 1]
    maxG = int(maxG)
    iterator = 0
    while iterator < len(yearFilter):
        if maxG < int(yearFilter[iterator][5]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "g-min" in sys.argv:
    minG = sys.argv[sys.argv.index("g-min") + 1]
    minG = int(minG)
    iterator = 0
    while iterator < len(yearFilter):
        if minG > int(yearFilter[iterator][5]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "ab-max" in sys.argv:
    maxAB = sys.argv[sys.argv.index("ab-max") + 1]
    maxAB = int(maxAB)
    iterator = 0
    while iterator < len(yearFilter):
        if maxAB < int(yearFilter[iterator][6]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "ab-min" in sys.argv:
    minAB = sys.argv[sys.argv.index("ab-min") + 1]
    minAB = int(minAB)
    iterator = 0
    while iterator < len(yearFilter):
        if minAB > int(yearFilter[iterator][6]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "r-max" in sys.argv:
    maxR = sys.argv[sys.argv.index("r-max") + 1]
    maxR = int(maxR)
    iterator = 0
    while iterator < len(yearFilter):
        if maxR < int(yearFilter[iterator][7]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "r-min" in sys.argv:
    minR = sys.argv[sys.argv.index("r-min") + 1]
    minR = int(minR)
    iterator = 0
    while iterator < len(yearFilter):
        if minR > int(yearFilter[iterator][7]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "h-max" in sys.argv:
    maxH = sys.argv[sys.argv.index("h-max") + 1]
    maxH = int(maxH)
    iterator = 0
    while iterator < len(yearFilter):
        if maxH < int(yearFilter[iterator][8]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "h-min" in sys.argv:
    minH = sys.argv[sys.argv.index("h-min") + 1]
    minH = int(minH)
    iterator = 0
    while iterator < len(yearFilter):
        if minH > int(yearFilter[iterator][8]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "2b-max" in sys.argv:
    max2B = sys.argv[sys.argv.index("2b-max") + 1]
    max2B = int(max2B)
    iterator = 0
    while iterator < len(yearFilter):
        if max2B < int(yearFilter[iterator][9]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "2b-min" in sys.argv:
    min2B = sys.argv[sys.argv.index("2b-min") + 1]
    min2B = int(min2B)
    iterator = 0
    while iterator < len(yearFilter):
        if min2B > int(yearFilter[iterator][9]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "3b-max" in sys.argv:
    max3B = sys.argv[sys.argv.index("3b-max") + 1]
    max3B = int(max3B)
    iterator = 0
    while iterator < len(yearFilter):
        if max3B < int(yearFilter[iterator][10]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "3b-min" in sys.argv:
    min3B = sys.argv[sys.argv.index("3b-min") + 1]
    min3B = int(min3B)
    iterator = 0
    while iterator < len(yearFilter):
        if min3B > int(yearFilter[iterator][10]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "hr-max" in sys.argv:
    maxHR = sys.argv[sys.argv.index("hr-max") + 1]
    maxHR = int(maxHR)
    iterator = 0
    while iterator < len(yearFilter):
        if maxHR < int(yearFilter[iterator][11]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "hr-min" in sys.argv:
    minHR = sys.argv[sys.argv.index("hr-min") + 1]
    minHR = int(minHR)
    iterator = 0
    while iterator < len(yearFilter):
        if minHR > int(yearFilter[iterator][11]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "rbi-max" in sys.argv:
    maxRBI = sys.argv[sys.argv.index("rbi-max") + 1]
    maxRBI = int(maxRBI)
    iterator = 0
    while iterator < len(yearFilter):
        if maxRBI < int(yearFilter[iterator][12]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "rbi-min" in sys.argv:
    minRBI = sys.argv[sys.argv.index("rbi-min") + 1]
    minRBI = int(minRBI)
    iterator = 0
    while iterator < len(yearFilter):
        if minRBI > int(yearFilter[iterator][12]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "sb-max" in sys.argv:
    maxSB = sys.argv[sys.argv.index("sb-max") + 1]
    maxSB = int(maxSB)
    iterator = 0
    while iterator < len(yearFilter):
        if maxSB < int(yearFilter[iterator][13]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "sb-min" in sys.argv:
    minSB = sys.argv[sys.argv.index("sb-min") + 1]
    minSB = int(minSB)
    iterator = 0
    while iterator < len(yearFilter):
        if minSB > int(yearFilter[iterator][13]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "cs-max" in sys.argv:
    maxCS = sys.argv[sys.argv.index("cs-max") + 1]
    maxCS = int(maxCS)
    iterator = 0
    while iterator < len(yearFilter):
        if maxCS < int(yearFilter[iterator][14]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "cs-min" in sys.argv:
    minCS = sys.argv[sys.argv.index("cs-min") + 1]
    minCS = int(minCS)
    iterator = 0
    while iterator < len(yearFilter):
        if minCS > int(yearFilter[iterator][14]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "bb-max" in sys.argv:
    maxBB = sys.argv[sys.argv.index("bb-max") + 1]
    maxBB = int(maxBB)
    iterator = 0
    while iterator < len(yearFilter):
        if maxBB < int(yearFilter[iterator][15]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "bb-min" in sys.argv:
    minBB = sys.argv[sys.argv.index("bb-min") + 1]
    minBB = int(minBB)
    iterator = 0
    while iterator < len(yearFilter):
        if minBB > int(yearFilter[iterator][15]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "so-max" in sys.argv:
    maxSO = sys.argv[sys.argv.index("so-max") + 1]
    maxSO = int(maxSO)
    iterator = 0
    while iterator < len(yearFilter):
        if maxSO < int(yearFilter[iterator][16]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "so-min" in sys.argv:
    minSO = sys.argv[sys.argv.index("so-min") + 1]
    minSO = int(minSO)
    iterator = 0
    while iterator < len(yearFilter):
        if minSO > int(yearFilter[iterator][16]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "ibb-max" in sys.argv:
    maxIBB = sys.argv[sys.argv.index("ibb-max") + 1]
    maxIBB = int(maxIBB)
    iterator = 0
    while iterator < len(yearFilter):
        if maxIBB < int(yearFilter[iterator][17]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "ibb-min" in sys.argv:
    minIBB = sys.argv[sys.argv.index("ibb-min") + 1]
    minIBB = int(minIBB)
    iterator = 0
    while iterator < len(yearFilter):
        if minIBB > int(yearFilter[iterator][17]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "hbp-max" in sys.argv:
    maxHBP = sys.argv[sys.argv.index("hbp-max") + 1]
    maxHBP = int(maxHBP)
    iterator = 0
    while iterator < len(yearFilter):
        if maxHBP < int(yearFilter[iterator][18]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "hbp-min" in sys.argv:
    minHBP = sys.argv[sys.argv.index("hbp-min") + 1]
    minHBP = int(minHBP)
    iterator = 0
    while iterator < len(yearFilter):
        if minHBP > int(yearFilter[iterator][18]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "sh-max" in sys.argv:
    maxSH = sys.argv[sys.argv.index("sh-max") + 1]
    maxSH = int(maxSH)
    iterator = 0
    while iterator < len(yearFilter):
        if maxSH < int(yearFilter[iterator][19]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "sh-min" in sys.argv:
    minSH = sys.argv[sys.argv.index("sh-min") + 1]
    minSH = int(minSH)
    iterator = 0
    while iterator < len(yearFilter):
        if minSH > int(yearFilter[iterator][19]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "sf-max" in sys.argv:
    maxSF = sys.argv[sys.argv.index("sf-max") + 1]
    maxSF = int(maxSF)
    iterator = 0
    while iterator < len(yearFilter):
        if maxSF < int(yearFilter[iterator][20]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "sf-min" in sys.argv:
    minSF = sys.argv[sys.argv.index("sf-min") + 1]
    minSF = int(minSF)
    iterator = 0
    while iterator < len(yearFilter):
        if minSF > int(yearFilter[iterator][20]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "gidp-max" in sys.argv:
    maxGIDP = sys.argv[sys.argv.index("gidp-max") + 1]
    maxGIDP = int(maxGIDP)
    iterator = 0
    while iterator < len(yearFilter):
        if maxGIDP < int(yearFilter[iterator][21]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

if "gidp-min" in sys.argv:
    minGIDP = sys.argv[sys.argv.index("gidp-min") + 1]
    minGIDP = int(minGIDP)
    iterator = 0
    while iterator < len(yearFilter):
        if minGIDP > int(yearFilter[iterator][21]):
            del(yearFilter[iterator])
            iterator = iterator - 1
        iterator = iterator + 1

header = ["playerID", "yearId", "stint", "teamID", "lgID", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", "CS", "BB", "SO", "IBB", "HBP", "SH", "SF", "GIDP"]
testFilter.append(header)

iterator = 0
while iterator < len(yearFilter) - 3:
    testPass = True
    if(yearFilter[iterator][0] != yearFilter[iterator + 1][0] or int(yearFilter[iterator][1]) != (int(yearFilter[iterator + 1][1]) - 1) or int(yearFilter[iterator][1]) != (int(yearFilter[iterator + 2][1]) - 2) or int(yearFilter[iterator][1]) != (int(yearFilter[iterator + 3][1]) - 3)):
        testPass = False
    if testPass:
        testFilter.append(yearFilter[iterator])
        testFilter.append(yearFilter[iterator + 1])
        testFilter.append(yearFilter[iterator + 2])
        testFilter.append(yearFilter[iterator + 3])
    iterator = iterator + 1

writecsv(testFilter)
