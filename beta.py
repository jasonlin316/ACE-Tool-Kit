import os
import time
#5386:pin to taskbar
#5387:unpin from taskbar

#school:word, excel, powerpoint
#office:word, excel, powerpoint, outlook, skype
#home:spotify, netflix

a=1
new_mode = 0
curr_mode = 0

apps = []

school = []
office = []
home   = []

office.append("C:\Windows\\notepad.exe")
office.append("C:\Windows\\System32\\calc.exe") #skype
apps.append(office)

school.append("C:\Windows\\System32\\calc.exe")
school.append("C:\Windows\\System32\\EXCEL.EXE")
school.append("C:\Windows\\System32\\WINWORD.EXE")
apps.append(school)

home.append("C:\Windows\\System32\\WINWORD.EXE")
apps.append(home)

def mode_change(curr_mode,new_mode):
    curr_str = ''
    new_str = ''
    cmd = ''
    

    for i in range(len(apps[curr_mode])):
        curr_str += 'syspin "'
        curr_str += apps[int(curr_mode)][i]
        curr_str += '" 5837 && '
    
    for i in range(len(apps[int(new_mode)])):
        new_str += 'syspin "'
        new_str += apps[int(new_mode)][i]
        if i == len(apps[int(new_mode)])-1:
            new_str += '" 5836" '
        else:
            new_str += '" 5836 && '

    cmd = ' cmd /c "' + curr_str + new_str
    print(cmd)
    os.system(cmd)


while True:
    new_mode = input('enter mode:')

    try:
        new_mode = int(new_mode)
    except ValueError:
        break

    if new_mode != curr_mode:
        mode_change(curr_mode,new_mode)

    curr_mode = new_mode