from heuristicStructure import *
# Tests to ensure a heuristic will be defined, stored, and accessed correctly
test=Heuristic()
test.Monday=Day() # No args, should set business level on monday to 3 for all hours
for i in range(24):
    if(test.lookupBaseVal(0,i) != 3):
        raise Exception("ERROR: Found incorrect value in heuristic")

test.Tuesday=Day((0,5),(12,0))
for i in range(12):
    if(test.lookupBaseVal(1,i) != 5):
        raise Exception("ERROR: Found incorrect value in heuristic")

for i in range(12, 24):
    if(test.lookupBaseVal(1,i) != 0):
        print(test.lookupBaseVal(1,i))
        raise Exception("ERROR: Found incorrect value in heuristic")
