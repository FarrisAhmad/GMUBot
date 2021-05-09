from lotStructure import *
#This tests to see if the findBestLot and restoreNormality functions work as expected
testLots=LotList()
testLots.appendLot("A")
testLots.appendLot("B")
testLots.appendLot("C")

myLot= testLots.lookup("B")
myLot.trend-=1

testResult= testLots.findBestLot()

if(testResult.name != myLot.name):
    raise Exception("ERROR: Lot found is not the optimal lot")

testLots.restoreNormality()

if(myLot.trend != 0):
    raise Exception("ERROR: Did not restore trend value to 0")
