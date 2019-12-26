import datetime

print("The default mode is HOME.")
SET=0
while SET==0:
    a=input("Set other modes (Y/N): ")
    if a=='y' or a=='Y':
        SET=1
    elif a=='n' or a=='N':
        SET=-1
    else:
        print("/* Please enter Y or N */")

print('-'*30)

class WEEK:
    def __init__(self, day, period=None, schedule=None):
        self.day=day #Weekday
        self.period=[0]
        self.schedule={0:'home'} #corresponding mode
    def set_schedule(self, mode, start, end):
        self.period.append(start)
        self.period.append(end)
        self.schedule[start]=mode
        self.schedule[end]='home'
    def reset(self):
        self.period.clear()
        self.schedule.clear()
        self.period=[0]
        self.schedule={0:'home'}

Weekday=[WEEK('Monday'),WEEK('Tuesday'),WEEK('Wednesday'),WEEK('Thursday'), WEEK('Friday'), WEEK('Saturday'), WEEK('Sunday')]

class MODE:
    
    def __init__(self, name):
        self.name=name
  
    def setting(self):
        print("Set", self.name, "mode")
        arr=input("Weekday (1 2 ... 7): ")
        self.day=[(int(n)-1) for n in arr.split()]
        self.time=[int(input("Start from (HHMM): "))]
        self.time.append(int(input("Until (HHMM): ")))
        print('-'*30)
        self.fill_in()

    def fill_in(self):
        if self.time[0]>self.time[1]:#if it cross the night
            for num in self.day:
                Weekday[num].set_schedule(self.name, self.time[0], 2400)
                Weekday[(num+1)%7].set_schedule(self.name, 0000, self.time[1])
        else:
            for num in self.day:
                Weekday[num].set_schedule(self.name, self.time[0], self.time[1])
        a=input("Other days and time? (Y/N): ")
        if a=='y' or a=='Y':#add other time setting
            self.setting()


while SET>0:
    modetype=['office', 'school', 'new']
    Mode=[]
    for i in range(0, 3):
        Mode.append(MODE(modetype[i]))
    SET=0#initiate

while SET>=0: #start settting
    print("Set", modetype[SET], end=' ')
    a=input("mode (Y/N): ")
    print('-'*30)
    if a=='y' or a=='Y':
        if SET==2:
            modetype[SET]=input("Mode name: ")
            Mode[SET].name=modetype[SET]
        Mode[SET].setting()
        SET+=1
    elif a=='n' or a=='N':
        SET+=1
    else:
        print("/* Please enter Y or N */")
    
    while SET>2: #finish
        a=input("Set again (Y/N): ")
        print('-'*30)
        if a=='y' or a=='Y':    
            for i in range(0,7):
                (Weekday[i]).reset()
                SET=0
        elif a=='n' or a=='N':
            SET=-1
        else:
            print("/* Please enter Y or N */")
    
   
for i in range(0,7):
    (Weekday[i]).period.sort()

now = datetime.datetime.now() #get current time
print(now.strftime('%Y-%m-%d %H:%M'),'\n')

WDay=now.isoweekday()-1 #get weekday
HR=now.hour*100 #get hour
MIN=now.minute #get minute
nowT=HR+MIN

while True:
    print("Today is", Weekday[WDay].day,'.')

    T=0
    for t in Weekday[WDay].period:
        if nowT<t and nowT>=T:
            break
        T=t

    print("Mode:", Weekday[WDay].schedule[T])
    print('-'*30)
    WDay=int(input("Weekday: "))-1
    nowT=int(input("Time: "))
    print('-'*30)#show the result
