import sys
import datetime
class Heuristic():
    "Structure to handle lookups for a given day and hour. returns expected fullness"
    def __init__(self):
        "Loads a default heuristic, with general expected parking filledness"
        self.Monday=Day((0,1),(8,3),(9,4),(17,3),(18,2), (19,1))
        self.Tuesday=Day((0,1),(8,3),(9,4),(17,3),(18,2), (19,1))
        self.Wednesday=Day((0,1),(8,3),(9,4),(17,3),(18,2), (19,1))
        self.Thursday=Day((0,1),(8,3),(9,4),(17,3),(18,2), (19,1))
        self.Friday=Day((0,1),(8,3),(9,4),(17,3),(18,2), (19,1))
        self.Saturday=Day((0,1),(8,2),(9,3),(13,2),(18,1))
        self.Sunday=Day((0,1),(8,2),(9,3),(13,2),(18,1))

    def lookupBaseVal(self, day, time):
        "Returns how busy the heuristic expect parking to be"
        if(time > 23 or time < 0):
            return -1
        if(isinstance(day, int)): #Not sure if passing string or int for day, handles both
            if(day==6): #Sunday
                return self.Sunday.hour[time]
            elif(day==0): #Monday
                return self.Monday.hour[time]
            elif(day==1): #Tuesday
                return self.Tuesday.hour[time]
            elif(day==2): #Wednesday
                return self.Wednesday.hour[time]
            elif(day==3): #Thursday
                return self.Thursday.hour[time]
            elif(day==4): #Friday
                return self.Friday.hour[time]
            elif(day==5): #Saturday
                return self.Saturday.hour[time]
        elif(isinstance(day, str)): #Code is passed an integer, this is dead code, but improves program flexibility
            day=day.lower().strip() #Formatting
            if(day=="sunday" or day=="sun"): #Sunday
                return self.Sunday.hour[time]
            elif(day=="monday" or day=="mon"): #Monday
                return self.Monday.hour[time]
            elif(day=="tuesday" or day=="tues"): #Tuesday
                return self.Tuesday.hour[time]
            elif(day=="wednesday" or day=="wed"): #Wednesday
                return self.Wednesday.hour[time]
            elif(day=="thursday" or day=="thur"): #Thursday
                return self.Thursday.hour[time]
            elif(day=="friday" or day=="fri"): #Friday
                return self.Friday.hour[time]
            elif(day=="saturday" or day=="sat"): #Saturday
                return self.Saturday.hour[time]
        else:
            return -1

class Day():
    "Given day of the week, holds int from 0-5 on how busy it is expected to be"
    def __init__(self, *args):
        "Given a list of tuples in form (hour, busy-level), defines a time range"
        self.hour=[-1]*24;
        self.month=None
        self.calendarDay=None
        self.next=None
        for times in args: #Define each specified hour
            if(isinstance(times[0], tuple)):
                for inner in times: # Called from dates
                    self.hour[max(0,min(inner[0], 23))]= max(0,min(inner[1], 5))
            else: # 
                self.hour[max(0,min(times[0], 23))]= max(0,min(times[1], 5))
        # generalizing ranges
        base=3
        for i in range(len(self.hour)):
            if(self.hour[i] ==-1):
                self.hour[i]=base
            else:
                base=self.hour[i]

    def pointUpdate(self, hourTime, newRate):
        "Updates day's projected business with the new rate"
        if(hourTime < 24 and hourTime >=0):
            self.hour[hourTime]=newRate
            return True
        return False

class Dates():
    "Class to store special days where their will be a different schedule, determiined by input"
    def __init__(self):
        "Simple Linked list"
        self.head=None

    def addDate(self, month, calendarDay, *schedule):
        "Accepts month (int) and calendar day, and schedule, a series of tuples (hour, level))"
        if(len(schedule)==0):
            specialDay= Day((0,1),(8,4),(9,5),(17,3),(18,2), (19,1))
        else:
            specialDay=Day(schedule)
        specialDay.month=month
        specialDay.calendarDay=calendarDay
        if(self.head is None):
            self.head= specialDay
        else: #Search for same date, if found delete and update
            deleteDate(month,calendarDay)
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=specialDay
    def removeOldDates(self):
        "Traverse List and remove any matching from the list"
        currentMonth=datetime.datetime.today().month
        currentDay=datetime.datetime.today().day
        current=self.head
        if(current is None):
            return
        if(current.month>=month and current.calendarDay>=calendarDay):
            self.head=current.next
            return
        prev=self.head
        current=prev.next
        while(current is not None):
            if(current.month>=month and current.calendarDay>=calendarDay):
                prev.next=current.next
            current=current.next

    def deleteDate(month,calendarDay):
        current=self.head
        if(current is None):
            return
        if(current.month==month and current.calendarDay==calendarDay):
            self.head=current.next
            return
        prev=self.head
        current=prev.next
        while(current is not None):
            if(current.month==month and current.calendarDay==calendarDay):
                prev.next=current.next
            current=current.next
        return














