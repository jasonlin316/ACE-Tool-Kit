import os

taskbar=['calc','mspaint']

apps = []

school = []
office = []
home   = []

office.append("mspaint.exe")
office.append("calc.exe") #skype
apps.append(office)

school.append("calc.exe")
school.append("EXCEL.EXE")
school.append("WINWORD.EXE")
apps.append(school)

home.append("WINWORD.EXE")
apps.append(home)

new_mode = 0
curr_mode = 0
           
cmd='cmd /c "'
def pin(new_mode): #pin
    global cmd
    for i in range(len(apps[new_mode])):
        cmd=cmd+'syspin "C:\Windows\\System32\\'+apps[new_mode][i]+'" 5386 '
        if i!=len(apps[new_mode])-1:
            cmd=cmd+'&& '
        else:
            cmd=cmd+'"'
    os.system(cmd)
    cmd = '' 

def unpin(curr_mode): #unpin
    global cmd
    for i in range(len(apps[curr_mode])):
        cmd=cmd+'syspin "C:\Windows\\System32\\'+apps[curr_mode][i]+'" 5387 '
        if i!=len(apps[curr_mode])-1:
            cmd=cmd+'&& '
        else:
            cmd=cmd+'"'
    os.system(cmd)
    cmd = '' 

while True:
    new_mode = input('enter mode:')

    try:
        new_mode = int(new_mode)
    except ValueError:
        break

    if new_mode != curr_mode:
        unpin(curr_mode)
        pin(new_mode)

    curr_mode = new_mode
#
##5386:pin to taskbar
##5387:unpin from taskbar
#
