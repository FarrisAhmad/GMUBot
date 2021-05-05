from lotStructure import *

masonLots=LotList()
masonLots.appendLot("A")
masonLots.appendLot("B")
masonLots.appendLot("C")
masonLots.appendLot("D")
masonLots.appendLot("E")
masonLots.appendLot("F")
myLot=masonLots.lookup("C")
myLot=masonLots.lookup("Nonsense") #Will set myLot to None
myLot=masonLots.lookup("C")
print(masonLots.buildUpdateMessage(["a","b","d"]))
myLot.trend+=2
print(masonLots.buildUpdateMessage([myLot.name, "Corn"]))
print(masonLots.parseMessage("Request C A B"))
print("")
print(masonLots.buildUpdateMessage())
masonLots.parseMessage("status FrEE")
masonLots.parseMessage("status FrEE")
print(masonLots.buildUpdateMessage())
