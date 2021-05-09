from lotStructure import *
#Tests to ensure the append and lookup function work as expected
testLots=LotList()
testLots.appendLot("A")
testLots.appendLot("B")
testLots.appendLot("C")
testLots.appendLot("D")
testLots.appendLot("E")
testLots.appendLot("F")

if(testLots.lookup("cactus") is not None):
    raise Exception("ERROR: Successful search for non-existant list")

if(testLots.lookup("A") is None):
    raise Exception("ERROR: unsuccessful search for lot name within list")

if(testLots.lookup("B") is None):
    raise Exception("ERROR: unsuccessful search for lot name within list")

if(testLots.lookup("C") is None):
    raise Exception("ERROR: unsuccessful search for lot name within list")

if(testLots.lookup("D") is None):
    raise Exception("ERROR: unsuccessful search for lot name within list")

if(testLots.lookup("E") is None):
    raise Exception("ERROR: unsuccessful search for lot name within list")

if(testLots.lookup("F") is None):
    raise Exception("ERROR: unsuccessful search for lot name within list")

if(testLots.lookup("c") is None):
    raise Exception("ERROR: unsuccessful search for lot name within list")

if(testLots.lookup("G") is not None):
    raise Exception("ERROR: Successful search for non-existant list")


