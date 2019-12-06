import os

taskbar=['calc','mspaint']

#os.system('cmd /k "syspin "C:\Windows\\System32\\calc.exe\" 5386 && "')   
              
cmd='cmd /k "'
def pin(): #pin
    global cmd
    for i in range(len(taskbar)):
        cmd=cmd+'syspin "C:\Windows\\System32\\'+taskbar[i]+'.exe\" 5386 '
        if i!=len(taskbar)-1:
            cmd=cmd+'&& '
        else:
            cmd=cmd+'"'
        
def unpin(): #unpin
    global cmd
    for i in range(len(taskbar)):
        cmd=cmd+'syspin "C:\Windows\\System32\\'+taskbar[i]+'.exe\" 5387 '
        if i!=len(taskbar)-1:
            cmd=cmd+'&& '
        else:
            cmd=cmd+'"'
        
#    syspin "C:\Windows\\System32\\'+taskbar[0]+'.exe\" 5386 &&  \
#    syspin "C:\Windows\\'+taskbar[1]+'.exe\" 5386 \
#    "'
pin()
print(cmd)
os.system(cmd)
#
##5386:pin to taskbar
##5387:unpin from taskbar
#
##school:word, excel, powerpoint
##office:word, excel, powerpoint, outlook, skype
##home:spotify, netflix
#
#a=1
#
#if a==1: #school-->office
#    os.system('cmd /k "\
#              syspin "C:\Windows\\System32\\outlook.exe\" 5386  && \
#              syspin "C:\Windows\\System32\\skype.exe\" 5386 \
#              "')
#    
#elif a==2: #school-->home
#    os.system('cmd /k "\
#              syspin "C:\Windows\\Systim32\\word.exe\" 5387  && \
#              syspin "C:\Windows\\System32\\excel.exe\" 5387 && \
#              syspin "C:\Windows\\System32\\powerpnt.exe\" 5387 && \
#              syspin "C:\Windows\\System32\\spotify.exe\" 5386 && \
#              syspin "C:\Windows\\System32\\netflix.exe\" 5386 && \
#              "')
#    
#elif a==3: #office-->home
#    os.system('cmd /k "\
#              syspin "C:\Windows\\Systim32\\word.exe\" 5387  && \
#              syspin "C:\Windows\\System32\\excel.exe\" 5387 && \
#              syspin "C:\Windows\\System32\\powerpnt.exe\" 5387 && \
#              syspin "C:\Windows\\System32\\skype.exe\" 5387  && \
#              syspin "C:\Windows\\System32\\outlook.exe\" 5387 \
#              syspin "C:\Windows\\System32\\spotify.exe\" 5386 && \
#              syspin "C:\Windows\\System32\\netflix.exe\" 5386 && \
#              "')
#    
#elif a==4: #office-->school
#    os.system('cmd /k "\
#              syspin "C:\Windows\\System32\\skype.exe\" 5387  && \
#              syspin "C:\Windows\\System32\\outlook.exe\" 5387 \
#              "')
#    
#elif a==5: #home-->school
#    os.system('cmd /k "\
#              syspin "C:\Windows\\System32\\spotify.exe\" 5387 && \
#              syspin "C:\Windows\\System32\\netflix.exe\" 5387 && \
#              syspin "C:\Windows\\Systim32\\word.exe\" 5386  && \
#              syspin "C:\Windows\\System32\\excel.exe\" 5386 && \
#              syspin "C:\Windows\\System32\\powerpnt.exe\" 5386 && \
#              "')
#    
#elif a==6: #home-->office
#    os.system('cmd /k "\
#              syspin "C:\Windows\\System32\\spotify.exe\" 5387 && \
#              syspin "C:\Windows\\System32\\netflix.exe\" 5387 && \
#              syspin "C:\Windows\\Systim32\\word.exe\" 5386  && \
#              syspin "C:\Windows\\System32\\excel.exe\" 5386 && \
#              syspin "C:\Windows\\System32\\powerpnt.exe\" 5386 && \
#              syspin "C:\Windows\\System32\\outlook.exe\" 5386  && \
#              syspin "C:\Windows\\System32\\skype.exe\" 5386 \
#              "')
    