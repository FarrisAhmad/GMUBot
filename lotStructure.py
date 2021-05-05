import sys
from heuristicStructure import *
import datetime

class Lot:
    "Nodes for a list of each lot, each will hold an integer revealing its current status"
    def __init__(self, name):
        self.name=str.upper(name)
        self.expected=Heuristic()
        self.trend=0
        self.next=None

    def scoreLot(self, day, time):
        "Simple function that returns a the score of how busy a lot is. Lower is more desirable"
        return max(min(5,self.expected.lookupBaseVal(day,time)+self.trend),0)

class LotList:
    "Simple Linked List connecting all Lots together. Used for printing and accessing"
    def __init__(self):
        "Lot List contains both a head pointer and a tail pointer to keep append func quick"
        self.head=None
        self.tail=None
    def inList(self, name):
        "Returns True of false whether or not name is in list (prevents redeclaring) ignores capitalization"
        current= self.head
        while(current is not None):
            if(current.name==name.upper()):
                return current
            current=current.next
        return None

    def restoreNormality(self):
        "Reduces all lots trend to be closer to 0 each call (if at 0, it will do nothing)"
        current=self.head
        while(current is not None):
            if(current.trend < 0):
                current.trend +=1
            elif(current.trend > 0):
                current.trend -=1
            current=current.next

    def appendLot(self, lotName):
        "Standard append function for a linked list. Adds Lot class to end of list."
        newLot=Lot(lotName)
        if(self.inList(lotName)): #Already within list
            return 
        if(self.head is None):
            self.head=newLot
            self.tail=newLot
            return
        current=self.tail
        current.next=newLot
        self.tail=current.next
    
    def findBestLot(self):
        "Traverse List and calculate a score for each lot at the given time, return that score"
        time=datetime.datetime.today().hour
        day=datetime.datetime.today().weekday()
        if(self.head is None):
            return
        current= self.head
        best=current
        bestScore=best.scoreLot(day,time)
        current=current.next
        while(current is not None):
            if(bestScore > current.scoreLot(day,time)):
                best=current
                bestScore=current.scoreLot(day,time)
            current=current.next
        return best

    def generalUpdate(self, value=1):
        "Updates the busy level of all lots by the given value (default +1). Values capped at 0 & 5"
        current=self.head
        while(current is not None):
            current.trend=value+current.trend
            current=current.next

    def buildUpdateMessage(self, lotNames=None):
        "Builds message with specified lot names. If there is no match or request is empty, includes all"
        time=datetime.datetime.today().hour
        day=datetime.datetime.today().weekday()
        noMatches=True
        tweet="LOT\tPOPULARITY\n"
        if(lotNames is None):
                current=self.head
                while(current is not None):
                    tweet+=current.name+"\t"+str(current.scoreLot(day,time))+"\n"
                    current=current.next
        else:
            for name in lotNames:
                #Given as list, break down further
                for lot in name:
                    test=self.inList(lot)
                    if(test is not None):
                        noMatches=False
                        tweet+=test.name+"\t"+str(test.scoreLot(day,time))+"\n"
        return tweet

    def lookup(self, lotName):
        "Traverse lots and find lot of matching name. return that lot"
        current=self.head
        while(current is not None):
            if(lotName.upper() == current.name):
                return current
            current=current.next
        return None

    def parseMessage(self, message):
        "Given a string, looks through a message to extract data or hear request"
        request=True
        feed=True
        try:
            f = open("requestKeywords.txt", "r")
            requestKeywords=buildKeywordList(f)
            f.close
        except:
            request=False
        try:
            g= open("feedKeywords.txt", "r")
            feedKeywords=buildKeywordList(g)
            g.close
        except:
            feed=False
        message=message.upper()
        msgFull=message
        #Words gathered in lists, now search message for each word. Look for structure
        # request Keyword followed by a series of names
        # feed keyword followed by series of name
        selectedList=[]
        if(request):
            for word in requestKeywords:
                pos=message.find(word.upper())
                if(pos!=-1):
                    #traverse rest of list for matches in lot names
                    message= message[pos:]
                    updates= message.split()
                    current= self.head
                    while(current is not None):
                        #search updates for 
                        if(current.name in updates):
                            selectedList.append(current.name)
                        current=current.next
                    return self.buildUpdateMessage(selectedList)
        #else, is a feed message or junk message
        if(feed):
            for word in feedKeywords:
                pos=message.find(word.upper())
                if(pos!=-1):
                    if("EMPTY" in msgFull or "FREE" in msgFull):
                        print("RECOGNIZED")
                        self.generalUpdate(-1)
                    else:
                        self.generalUpdate(1)
                    return None
        return None
                    


def buildKeywordList(srcFile):
    "Makes a list of keywords extracted from an opened file. Reads as 1 keyword per line in file, and assumes the file exists and can be read. Will remove any keywords that are empty or only contain white space"
    keywords= srcFile.read().splitlines()
    i=0
    for word in keywords:
        if(word.isspace() or not word):
            keywords.remove(word)
            i-=1
        else:
            keywords[i]=word.strip()
        word=word.upper()
        i+=1
    return keywords










